# Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом,
# чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.


class Fighter():
    def __init__(self,name):
        self.name = name
        self.weapon = None


    def equip_weapon(self, weapon):
            self.weapon = weapon
            print(f"{self.name} выбрал {self.weapon.name}.")

    def change_weapon(self, new_weapon):
        if self.weapon is not None:
            print(f"{self.name} сменил {self.weapon.name} на {new_weapon.name}.")
        else:
            print(f"{self.name} выбрал {new_weapon.name} в первый раз.")

        self.weapon = new_weapon

    def attack(self, monster):
        if self.weapon is not None:
            print(f"{self.name} наносит удар {self.weapon.name}.")
            monster.take_damage(self.weapon.damage)
        else:
            print(f"{self.name} не имеет оружия!")



class Monster():
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"{self.name} осталось здоровья: {self.health}")

class Weapon():
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage


class Sword(Weapon):
    def __init__(self):
        super().__init__("меч", 10)

class Bow(Weapon):
    def __init__(self):
        super().__init__("лук", 7)

class Axe(Weapon):
    def __init__(self):
        super().__init__("лук", 7)

# Создаем оружие
sword = Sword()
bow = Bow()
axe = Axe()


# Создаем бойца и монстра
fighter = Fighter("Иван")
monster = Monster("Орк", 15)

# Бой с мечом
fighter.equip_weapon(sword)
fighter.attack(monster)
fighter.change_weapon(axe)

# Бой с луком
fighter.equip_weapon(bow)
fighter.attack(monster)


