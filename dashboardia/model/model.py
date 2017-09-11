"""Model."""
# from copy import copy

from dashboardia import db


# TODO: Create models - Widget, View, Visualization, User, AppConfig, Module,
# Module_Marketplace

class Base(db.Model):
    """Abstract base model."""

    __abstract__ = True

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    metadata_store = db.Column(db.JSON)
    created_on = db.Column(db.DateTime, default=db.func.now(), index=True)
    updated_on = db.Column(db.DateTime, default=db.func.now(), index=True,
                           onupdate=db.func.now())

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __repr__(self):
        return '<Model \'{}\' of id \'{}\'.>'\
            .format(type(self).__name__, self.id)


class ModuleElementBase(Base):
    """Module Section."""

    __abstract__ = True

    name = db.Column(db.String(256), index=True, unique=True, nullable=False)
    description = db.Column(db.String(2000))
    icon = db.Column(db.String(256))
    label = db.Column(db.String(256), nullable=False)


class Ledger(Base):
    """Ledger."""

    __tablename__ = 'ledger'

    path = db.Column(db.String(256), index=True, nullable=False)
    name = db.Column(db.String(256), index=True, nullable=False)
    field = db.Column(db.String(256), index=True, nullable=False)
    value = db.Column(db.String(256))


class UI(Base):
    """UI."""

    __tablename__ = 'ui'

    name = db.Column(db.String(256), index=True, unique=True, nullable=False)
    value = db.Column(db.String(256))


class ModuleSection(ModuleElementBase):
    """Module Section."""

    __tablename__ = 'module_section'

    order = db.Column(db.Integer, index=True, unique=True)
    # - Note: Not sure the best value for 'lazy'. Dynamic is not good for
    # pre-loading values the way that is currently being done in the view_model
    # store. Seemingly good options are 'subquery', 'select', and 'joined'.
    # http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html
    children_dashboards = db.relationship('ModuleDashboard', backref='section',
                                          lazy='subquery')


class ModuleDashboard(ModuleElementBase):
    """Module Dashboard."""

    __tablename__ = 'module_dashboard'

    order = db.Column(db.Integer)
    parent_section_name = db.Column(db.String(256), db.ForeignKey(
        'module_section.name'), index=True, nullable=False)
    parent_section = db.relationship('ModuleSection')
