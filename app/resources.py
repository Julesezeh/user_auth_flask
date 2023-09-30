from .blueprint import app_bp
from flask import request, Response, render_template


@app_bp.register("/")
def index():
    return "Hello World"
