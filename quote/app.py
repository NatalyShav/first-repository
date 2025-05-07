from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Запрашиваем случайную цитату с API Forismatic
    response = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru')
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data['quoteText']
        author = quote_data['quoteAuthor'] if quote_data['quoteAuthor'] else "Неизвестный автор"
    else:
        quote = "Не удалось получить цитату."
        author = ""

    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)