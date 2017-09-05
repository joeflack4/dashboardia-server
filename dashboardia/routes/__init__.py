"""Routes."""
from flask import Blueprint, render_template

from ..config import TEMPLATE_DIR


client = Blueprint('client', __name__, template_folder=TEMPLATE_DIR)


@client.route('/')
def root():
    """Root."""
    return render_template('root.html')
