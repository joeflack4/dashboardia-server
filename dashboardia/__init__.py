"""Init."""
from os import getenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .routes import client
from .config import config


app = Flask(__name__)
app.config.from_object(config[getenv('APP_SETTINGS', 'default')])
db = SQLAlchemy()
db.init_app(app)
CORS(app)
app.static_folder = getenv('APP_STATIC_DIR', '../../client/assets')
app.register_blueprint(client)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
