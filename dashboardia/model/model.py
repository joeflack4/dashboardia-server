"""Model."""
from dashboardia import db


class Base(db.Model):
    """Abstract base model."""

    __abstract__ = True
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
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

    path = db.Column(db.String(256), index=True)
    name = db.Column(db.String(256), index=True)
    field = db.Column(db.String(256), index=True)
    metadata = db.Column(db.JSON)
    value = db.Column(db.String(256))

    def __init__(self, *args, **kwargs):
        """Init."""
        self.path = kwargs['path']
        self.name = kwargs['name']
        self.field = kwargs['field']
        self.metadata = kwargs['metadata']
        self.value = kwargs['value']
        super().__init__(*args, **kwargs)
