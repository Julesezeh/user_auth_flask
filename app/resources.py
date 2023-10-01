from .blueprint import app_bp
from app import logger
from flask import request, Response, render_template


@app_bp.register("/")
def index():
    logger.info("works fine")
    return "Hello World"
