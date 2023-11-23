from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'fortinaiti pabigi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from src import routes

# Функция для создания таблиц в контексте приложения
def create_tables():
    with app.app_context():
        db.create_all()

# Вызываем функцию для создания таблиц
create_tables()

if __name__ == "__main__":
    app.run(debug=True)
