"""Routes."""
from flask import Blueprint, render_template

from ..config import TEMPLATE_DIR


client = Blueprint('client', __name__, template_folder=TEMPLATE_DIR)


@client.route('/')
def root():
    """Root."""
    return home()


@client.route('/home')
def home():
    """Root."""
    return render_template('home.html')


@client.route('/settings')
def settings():
    """Settings."""
    return render_template('settings.html')


@client.route('/marketplace')
def marketplace():
    """Marketplace."""
    return render_template('marketplace.html')


@client.route('/dashboard')
def dashboard():
    """Dashboard."""
    return render_template('dashboard.html')


@client.route('/personal/settings')
def personal__settings():
    """personal__settings."""
    return render_template('sections/personal/settings.html')


@client.route('/personal/add')
def personal__add():
    """personal__add."""
    return render_template('sections/personal/add.html')


@client.route('/personal/social')
def personal__social():
    """personal__social."""
    return render_template('sections/personal/social.html')


@client.route('/personal/finance')
def personal__finance():
    """personal__finance."""
    return render_template('sections/personal/finance.html')


@client.route('/personal/health')
def personal__health():
    """personal__health."""
    return render_template('sections/personal/health.html')


@client.route('/learning/settings')
def learning__settings():
    """learning__settings."""
    return render_template('sections/learning/settings.html')


@client.route('/learning/add')
def learning__add():
    """Dashboard."""
    return render_template('sections/learning/add.html')


@client.route('/learning/something')
def learning__machine_learning_intro():
    """learning__machine_learning_intro."""
    return render_template('sections/learning/machine_learning_intro.html')
