"""Application manager."""
from flask_script import Manager, Shell

from dashboardia import app


manager = Manager(app)
shell_context = dict(app=app)
# shell_context = dict(app=app, db=db, MyModel=MyModel)
manager.add_command('shell', Shell(make_context=shell_context))


@manager.option('--overwrite', help='Drop tables first?', action='store_true')
def initdb(overwrite=False):
    """Create the database.

    Args:
        overwrite (bool): Overwrite database if True, else update.
    """
    with app.app_context():
        if overwrite:
            # db.drop_all()
            pass
        # db.create_all()
        if overwrite:
            pass


if __name__ == '__main__':
    manager.run()
