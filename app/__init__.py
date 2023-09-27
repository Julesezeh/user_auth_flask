from flask import Flask
from app.extensions import api, db, migration
from app.models import *
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    api.init_app(app)
    db.init_app(app)
    migration.init_app(app, db)
    # db.create_all()
    return app
