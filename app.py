from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Инициализация SQLAlchemy (без привязки к приложению)
db = SQLAlchemy()

def create_app():
    """Функция-фабрика для создания экземпляра приложения Flask."""
    app = Flask(__name__)
    
    # Настройка конфигурации базы данных (SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Инициализация расширения базы данных с текущим приложением
    db.init_app(app)
    
    # Создание контекста приложения для создания таблиц
    with app.app_context():
        # Создание всех таблиц базы данных (если они еще не существуют)
        db.create_all()
        
    return app

if __name__ == "__main__":
    app = create_app()
    # Запуск приложения в режиме отладки
    app.run(debug=True)