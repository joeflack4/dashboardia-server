"""Init."""
from os import getenv

from flask import Flask

from .routes import client
from .config import config


app = Flask(__name__)
app.config.from_object(config[getenv('APP_SETTINGS', 'default')])
app.static_folder = getenv('APP_STATIC_DIR', '../../client/assets')
app.register_blueprint(client)
