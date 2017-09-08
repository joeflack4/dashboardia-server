"""Application manager."""
from glob import glob
import csv

from flask_script import Manager, Shell
import xlrd

from dashboardia import app, db
from dashboardia.model import Ledger, UI


manager = Manager(app)
shell_context = dict(app=app, db=db)
ORDERED_MODEL_MAP = (
    ('ledger', Ledger),
    ('ui', UI)
)
manager.add_command('shell', Shell(make_context=shell_context))
for key, val in [mdl for mdl in ORDERED_MODEL_MAP]:
    shell_context[key] = val


# TODO: Add to joefuncs.
def get_file_by_glob(pattern):
    """Get file by glob.

    Args:
        pattern (str): A glob pattern.

    Returns:
        str: Path/to/first_file_found
    """
    return glob(pattern)[0]


SRC_DATA = get_file_by_glob('./data/data*.xlsx')


# TODO: Create package to import to DB from Excel file.
def init_from_source(path, model):
    """Initialize DB table data from csv file.

    Initialize table data from csv source data files associated with the
    corresponding data model.

    Args:
        path (str): Path to csv data file.
        model (class): SqlAlchemy model class.
    """
    with open(path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            record = model(**row)
            db.session.add(record)
        db.session.commit()


def init_from_sheet(ws, model):
    """Initialize DB table data from XLRD Worksheet.

    Initialize table data from source data associated with the corresponding
    data model.

    Args:
        ws (xlrd.sheet.Sheet): XLRD worksheet object.
        model (class): SqlAlchemy model class.
    """
    header = None
    for i, row in enumerate(ws.get_rows()):
        row = [r.value for r in row]
        if i == 0:
            header = row
        else:
            row_dict = {k: v for k, v in zip(header, row)}
            record = model(**row_dict)
            db.session.add(record)
    db.session.commit()


def init_from_workbook(wb, queue):
    """Init from workbook.

    Args:
        wb (xlrd.Workbook): Workbook object.
        queue (tuple): Order in which to load models.
    """
    with xlrd.open_workbook(wb) as book:
        for sheetname, model in queue:
            if sheetname == 'data':  # actually done last
                for ws in book.sheets():
                    if ws.name.startswith('data'):
                        init_from_sheet(ws, model)
            else:
                ws = book.sheet_by_name(sheetname)
                init_from_sheet(ws, model)


# TODO: remove --overwrite
@manager.option('--overwrite', help='Drop tables first?', action='store_true')
def initdb(overwrite=False):
    """Create the database.

    Args:
        overwrite (bool): Overwrite database if True, else update.
    """
    with app.app_context():
        if overwrite:
            db.drop_all()
        db.create_all()
        if overwrite:
            init_from_workbook(wb=SRC_DATA, queue=ORDERED_MODEL_MAP)


if __name__ == '__main__':
    manager.run()
