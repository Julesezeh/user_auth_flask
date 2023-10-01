from flask import Blueprint, Flask
import logging

app = Flask(__name__)
# logger = logging.getLogger(__name__)

app_bp = Blueprint("app_blueprint", __name__)


@app_bp.route("/")
def index():
    app.logger.info("Works fine")
    return "Hello World"
