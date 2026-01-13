from app.models.user import User
from app.models import db


def get_all_users():
    return User.query.all()



def create_user(name):
    if not name:
        raise ValueError("User name is required")

    user = User(name=name)
    db.session.add(user)
    db.session.commit()

    return user



def get_user_by_id(user_id):
    return User.query.get(user_id)



def update_user(user_id, new_name):
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("User not found")

    if not new_name:
        raise ValueError("User name is required")

    user.name = new_name
    db.session.commit()

    return user



def delete_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("User not found")

    db.session.delete(user)
    db.session.commit()