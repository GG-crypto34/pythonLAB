from flask import Blueprint, render_template
from app.models import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():

    return render_template("index.html")
