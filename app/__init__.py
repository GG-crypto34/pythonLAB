from flask import Flask
from .config import Config
from .models import db
from flask_migrate import Migrate

migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
