#Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.


class Store():

    def __init__(self,name, address, items = None):
        if items is None:
            items = {}
        self.name = name
        self.address = address
        self.items = items

    def add_item(self, name, price):
        if name in self.items:
            print(f"Товар '{name}' уже существует в магазине {self.name}. Обновите цену, если нужно.")
        else:
            self.items[name] = price
            print(f"Товар '{name}' добавлен магазин {self.name} с ценой {price:.2f}.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Товар '{name}' удален из магазина {self.name}.")
        else:
            print(f"Товар '{name}' не найден в магазине {self.name}.")

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
            print(f"Цена товара '{name}' в магазине {self.name} обновлена до {new_price:.2f}.")
        else:
            print(f"Товар '{name}'  в магазине {self.name} не найден.")

    def list_items(self):
        if not self.items:
            print(f"В магазине {self.name} нет товаров.")
        else:
            print(f"Товары в магазине {self.name} :")
            for name, price in self.items.items():
                print(f"{name}: {price:.2f}")

store1 = Store("Яндекс Маркет", "Москва, Шаболовка")
store1.add_item("Ноутбук", 55000)
store1.add_item("Смартфон", 30000)
store1.add_item("Планшет", 15000)
store1.list_items()

store2 = Store("WB", "Москва,Кремль")
store2.add_item("Книга 1", 500)
store2.add_item("Книга 2", 700)
store2.add_item("Книга 3", 300)
store2.list_items()

store3 = Store("OZON", "Москва, Лужники")
store3.add_item("Футболка", 1500)
store3.add_item("Джинсы", 2500)
store3.add_item("Кроссовки", 4000)
store3.list_items()