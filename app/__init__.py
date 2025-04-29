from flask import Flask

# Создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)
# Создаем секретный ключ для защиты данных
app.config['SECRET_KEY'] = 'your_secret_key'

# Импортируем маршруты после создания приложения
from app import routes