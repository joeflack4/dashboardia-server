"""Init."""
from os import getenv

from flask import Flask

from .routes import client
from .config import config


app = Flask(__name__)
app.config.from_object(config[getenv('APP_SETTINGS', 'default')])
app.static_folder = getenv('APP_STATIC_DIR', '../../client/assets')
app.register_blueprint(client)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
