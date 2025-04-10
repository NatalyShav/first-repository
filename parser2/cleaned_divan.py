import csv
import pandas as pd

# Чтение CSV файла
df = pd.read_csv('prices_div.csv')

def clean_price(price):
    if isinstance(price, str):  # Проверка, что price - строка
        # Удаление 'руб.' и пробелов
        cleaned_price = price.replace('руб.', '').replace(' ', '')
        # Пробуем преобразовать в число
        try:
            return int(cleaned_price)
        except ValueError:
            return None  # Возвращаем None в случае ошибки преобразования
    return None  # Если price не строка, возвращаем None

# Применение функции к столбцу Price
df['Price'] = df['Price'].apply(clean_price)

# Вычисление средней цены, исключая значения NaN
average_price = df['Price'].mean()

# Вывод средней цены
print(f'Средняя цена: {average_price:.2f} рублей')

# Сохранение результата в новый CSV файл
df.to_csv('cleaned_prices.csv', index=False)