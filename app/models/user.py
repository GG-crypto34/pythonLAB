from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    expenses = db.relationship(
    "Expense",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
)


    def __repr__(self):
        return f"<User {self.id} - {self.name}>"
    

