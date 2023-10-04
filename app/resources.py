import app
from flask import request, Response, render_template
from flask import current_app


@app.route("/")
def index():
    current_app.logger.info("Keep the streak alive")
    return "Hello World"
