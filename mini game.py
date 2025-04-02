# Мини-игра "Угадай слово", в которой компьютер дает описание значения слова  с сайта randomword.com на русском языке.
#Пользователь должен угадать слово и записать его по-английски.

from bs4 import BeautifulSoup
import requests
from googletrans import Translator

#Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        # Создаём объект Soup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


#Создаём функцию, которая будет делать саму игру

def word_game():
    print("Добро пожаловать в игру! Я буду тебе выдавать значение слова на русском языке,\n" "а ты должен угадать это слово и написать ответ на по-английски.")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # функция для перевода значения слова на русский язык
        translator = Translator()
        translate_word_definition = translator.translate(word_definition, dest="ru").text

        # Начинаем игру
        print(f"Значение слова - {translate_word_definition}")
        user = input("Что это за слово? ")
        if user.lower() == word.lower():
            print("Ответ верный")
        else:
            print(f"Ответ неверный. Было загадано это слово - {word}")


        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()


