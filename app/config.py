class Config:
    SECRET_KEY = "dev-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///expenses.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False