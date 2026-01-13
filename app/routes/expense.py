from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db
from app.models.expense import Expense
from app.models.user import User
from datetime import datetime
from app.services.expense_service import get_expenses_by_user, delete_expense
expense_bp = Blueprint('expense', __name__)

@expense_bp.route("/users/<int:user_id>/expenses")
def list_expenses(user_id):
    expenses = get_expenses_by_user(user_id)
    return render_template(
        "expenses/expense_list.html",
        expenses=expenses,
        user_id=user_id
    )

@expense_bp.route("/users/<int:user_id>/expenses/add", methods=["GET", "POST"])
def add_expense(user_id):
    if request.method == "POST":
        from app.services.expense_service import create_expense
        create_expense(
            user_id=user_id,
            category=request.form["category"],
            amount=request.form["amount"],
            date=request.form["date"],
            comment=request.form.get("comment"),
            payment_method=request.form["payment_method"],
        )
        return redirect(url_for("expense.list_expenses", user_id=user_id))

    return render_template("expenses/add_expense.html", user_id=user_id)

@expense_bp.route("/expenses/delete/<int:expense_id>")
def remove_expense(expense_id):
    try:
        delete_expense(expense_id)
    except ValueError as e:
        return str(e)

    return redirect(request.referrer)

@expense_bp.route("/expenses/edit/<int:expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)

    if request.method == "POST":
        from app.services.expense_service import update_expense

        update_expense(
            expense_id,
            request.form["category"],
            request.form["amount"],
            request.form["date"],
            request.form.get("comment"),
            request.form["payment_method"],
        )
        return redirect(url_for("expense.list_expenses", user_id=expense.user_id))

    return render_template("expenses/edit_expense.html", expense=expense)