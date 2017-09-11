"""Routes."""
from flask import Blueprint, render_template, jsonify

from ..config import TEMPLATE_DIR


client = Blueprint('client', __name__, template_folder=TEMPLATE_DIR)


@client.route('/')
def root():
    """Root."""
    return home()


@client.route('/store')
def store():
    """Data store."""
    from ..model.view_model import store
    return jsonify(store)


@client.route('/home')
def home():
    """Root."""
    from ..model.view_model import store
    return render_template('home.html', store=store)


@client.route('/settings')
def settings():
    """Settings."""
    from ..model.view_model import store
    return render_template('settings.html', store=store)


@client.route('/marketplace')
def marketplace():
    """Marketplace."""
    from ..model.view_model import store
    return render_template('marketplace.html', store=store)


@client.route('/personal/settings')
def personal__settings():
    """personal__settings."""
    from ..model.view_model import store
    return render_template('sections/personal/settings.html', store=store)


@client.route('/personal/add')
def personal__add():
    """personal__add."""
    from ..model.view_model import store
    return render_template('sections/personal/add.html', store=store)


@client.route('/personal/social')
def personal__social():
    """personal__social."""
    from ..model.view_model import store
    return render_template('sections/personal/social.html', store=store)


@client.route('/personal/finance')
def personal__finance():
    """personal__finance."""
    from ..model.view_model import store
    return render_template('sections/personal/finance.html', store=store)


@client.route('/personal/health')
def personal__health():
    """personal__health."""
    from ..model.view_model import store
    return render_template('sections/personal/health.html', store=store)


@client.route('/learning/settings')
def learning__settings():
    """learning__settings."""
    from ..model.view_model import store
    return render_template('sections/learning/settings.html', store=store)


@client.route('/learning/add')
def learning__add():
    """Dashboard."""
    from ..model.view_model import store
    return render_template('sections/learning/add.html', store=store)


@client.route('/learning/machine_learning_intro')
def learning__machine_learning_intro():
    """learning__machine_learning_intro."""
    from ..model.view_model import store
    return render_template('sections/learning/machine_learning_intro.html',
                           store=store)
