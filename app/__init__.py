from flask import Flask, app
from .config import Config
from .models import db
from flask_migrate import Migrate
from .errors import register_error_handlers

migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.main import main_bp
    from app.routes.expense import expense_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(expense_bp)
    register_error_handlers(app)  

    return app
