from . import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    comment = db.Column(db.String(200))
    payment_method = db.Column(db.String(20), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"<Expense {self.category} - {self.amount}>"