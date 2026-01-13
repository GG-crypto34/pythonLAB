from app.models.expense import Expense
from app.models.user import User
from app.models import db
from datetime import datetime



def get_expenses_by_user(user_id):
    return Expense.query.filter_by(user_id=user_id).all()



def create_expense(user_id, category, amount, date, comment, payment_method):
    if not category:
        raise ValueError("Category is required")

    if not amount or float(amount) <= 0:
        raise ValueError("Amount must be positive")

    if not date:
        raise ValueError("Date is required")

    if not payment_method:
        raise ValueError("Payment method is required")

    user = User.query.get(user_id)
    if not user:
        raise ValueError("User not found")

    expense = Expense(
        category=category,
        amount=float(amount),
        date=datetime.strptime(date, "%Y-%m-%d"),
        comment=comment,
        payment_method=payment_method,
        user_id=user_id
    )

    db.session.add(expense)
    db.session.commit()

    return expense



def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if not expense:
        raise ValueError("Expense not found")

    db.session.delete(expense)
    db.session.commit()


def update_expense(expense_id, category, amount, date, comment, payment_method):
    expense = Expense.query.get(expense_id)
    if not expense:
        raise ValueError("Expense not found")

    expense.category = category
    expense.amount = float(amount)
    expense.date = datetime.strptime(date, "%Y-%m-%d")
    expense.comment = comment
    expense.payment_method = payment_method

    db.session.commit()