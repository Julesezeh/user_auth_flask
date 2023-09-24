from flask import Flask
from app.extensions import api, db, migration
from app.models import *


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    api.init_app(app)
    db.init_app(app)
    migration.init_app(app, db)
    # db.create_all()
    return app
