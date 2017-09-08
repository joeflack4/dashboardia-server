"""Model."""
from copy import copy

from dashboardia import db


# TODO: Create models - Widget, View, Visualization, User, AppConfig, Module,
# Module_Marketplace, Module_Section, Module_Dashboard

class Base(db.Model):
    """Abstract base model."""

    __abstract__ = True
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    metadata_store = db.Column(db.JSON)
    created_on = db.Column(db.DateTime, default=db.func.now(), index=True)
    updated_on = db.Column(db.DateTime, default=db.func.now(), index=True,
                           onupdate=db.func.now())

    def __init__(self, *args, **kwargs):
        """Init."""
        # super().__init__(*args, **kwargs)
        pass


class Ledger(Base):
    """Ledger."""

    __tablename__ = 'ledger'
    metadata_store = copy(Base.metadata_store)
    path = db.Column(db.String(256), index=True, nullable=False)
    name = db.Column(db.String(256), index=True, nullable=False)
    field = db.Column(db.String(256), index=True, nullable=False)
    value = db.Column(db.String(256))

    def __init__(self, *args, **kwargs):
        """Init."""
        self.metadata = kwargs['metadata_store']
        self.path = kwargs['path']
        self.name = kwargs['name']
        self.field = kwargs['field']
        self.value = kwargs['value']
        super().__init__(*args, **kwargs)


class UI(Base):
    """Ledger."""

    __tablename__ = 'ui'
    metadata_store = copy(Base.metadata_store)
    name = db.Column(db.String(256), index=True, unique=True, nullable=False)
    value = db.Column(db.String(256))

    def __init__(self, *args, **kwargs):
        """Init."""
        self.metadata = kwargs['metadata_store']
        self.name = kwargs['name']
        self.value = kwargs['value']
        super().__init__(*args, **kwargs)
