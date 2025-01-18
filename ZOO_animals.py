#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal(): #Родительский класс для животных"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
       pass

    def eat(self):
        pass

class Bird(Animal): #Класс птицы

    def make_sound(self):
        print(f"{self.name} чирикает")

    def fly(self):
        print(f"{self.name} летает")


class Mammal(Animal): #Класс млекопитающее

    def make_sound(self):
        print(f"{self.name} рычит")

class Reptile(Animal):

    def make_sound(self):
        print(f"{self.name} молчит")

    def crawl(self):
        print(f"{self.name} ползает")

animals = [Bird("Птица", 1), Mammal("Млекопитающее", 2), Reptile("Ящерица", 3)]
for animal in animals:
    animal.make_sound()


parrot = Bird("Кеша",15)
parrot.fly()
parrot.make_sound()

leopard = Mammal("Лео", 1)
leopard.make_sound()

crocodile = Reptile("Николас", 25)
crocodile.make_sound()
crocodile.crawl()

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} добавлен в персонал зоопарка.")

    def show_animals(self):
        for animal in self.animals:
            print(f"Животное: {animal.name}, Возраст: {animal.age}")

    def show_staff(self):
        for member in self.staff:
            print(f"Сотрудник: {member.name}")

zoo = Zoo()

# Добавление животных
parrot = Bird("Кеша", 15)
leopard = Mammal("Лео", 1)
crocodile = Reptile("Николас", 25)

zoo.add_animal(parrot)
zoo.add_animal(leopard)
zoo.add_animal(crocodile)

# Добавление сотрудников
zookeeper = ZooKeeper("Ваня")
veterinarian = Veterinarian("Лида")

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

# Показываем животных и сотрудников
zoo.show_animals()
zoo.show_staff()

# Примеры взаимодействия сотрудников с животными
zookeeper.feed_animal(parrot)
veterinarian.heal_animal(leopard)

# Проверка звуков животных
for animal in zoo.animals:
    animal.make_sound()

