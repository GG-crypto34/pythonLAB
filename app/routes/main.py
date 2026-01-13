from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.services.user_service import (
    get_all_users,
    create_user,
    update_user,
    delete_user,
    get_user_by_id
)

from flask_login import login_required, current_user
from datetime import datetime
from ..models import Expense, db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    users = get_all_users()
    return render_template("index.html", users=users)


@main_bp.route("/users/add", methods=["POST"])
def add_user():
    name = request.form.get("name")

    try:
        create_user(name)
    except ValueError as e:
        return str(e)

    return redirect(url_for("main.index"))



@main_bp.route("/users/edit/<int:user_id>", methods=["POST"])
def edit_user(user_id):
    name = request.form.get("name")

    try:
        update_user(user_id, name)
    except ValueError as e:
        return str(e)

    return redirect(url_for("main.index"))



@main_bp.route("/users/delete/<int:user_id>")
def remove_user(user_id):
    try:
        delete_user(user_id)
    except ValueError as e:
        return str(e)

    return redirect(url_for("main.index"))


