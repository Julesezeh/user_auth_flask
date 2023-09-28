from flask import Blueprint


app_bp = Blueprint("app_blueprint", __name__)


@app_bp.route("/")
def index():
    return "Hello World"
