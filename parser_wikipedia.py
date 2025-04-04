from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация драйвера
browser = webdriver.Chrome()  # Убедитесь, что chromedriver находится в вашем PATH


def search_wikipedia(query):
    browser.get("https://ru.wikipedia.org/wiki/Главная_страница")
    search_box = browser.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Ждем загрузки страницы


def read_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
    print("\n")


def get_related_links():
    related_links = browser.find_elements(By.CSS_SELECTOR, ".mw-search-result-heading a")  # Получаем ссылки из параграфов
    return related_links  # Возвращаем список ссылок


def main():
    initial_query = input("Введите ваш запрос для поиска на Википедии: ")
    search_wikipedia(initial_query)

    # Получаем связанные статьи один раз
    related_links = get_related_links()

    while True:
        print("Выберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Ваш выбор (1, 2, 3): ")

        if choice == "1":
            read_paragraphs()
        elif choice == "2":
            related_links = get_related_links()
            print("Выберите связанную статью:")
            for i, link in enumerate(related_links[:3], start=1):  # Предлагаем три варианта
                print(f"{i}. {link.text}")

            selection = int(input("Ваш выбор (1, 2, 3): ")) - 1
            if 0 <= selection < len(related_links):
                selected_article = related_links[selection].text  # Сохраняем название выбранной статьи
                related_links[selection].click()
                time.sleep(5)  # Ждем загрузки страницы

                # После перехода на связанную статью, предоставляем возможность читать параграфы
                while True:
                    print(f"Вы сейчас читаете статью: '{selected_article}'")  # Выводим название статьи
                    print("Выберите действие:")
                    print("1. Листать параграфы текущей статьи")
                    print("2. Вернуться к списку связанных статей")
                    print("3. Выйти из программы")

                    sub_choice = input("Ваш выбор (1, 2, 3): ")

                    if sub_choice == "1":
                        read_paragraphs()
                    elif sub_choice == "2":
                        break  # Возвращаемся к выбору действий по основной статье
                    elif sub_choice == "3":
                        print("Выход из программы.")
                        browser.quit()
                        return
                    else:
                        print("Некорректный выбор. Попробуйте снова.")
            else:
                print("Некорректный выбор. Попробуйте снова.")
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
    browser.quit()