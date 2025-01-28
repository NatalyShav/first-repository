import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100  # Начальное значение здоровья
        self.attack_power = 20  # Начальная сила удара

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Геймер")

    def start(self):
        print("\nБитва началась!\n")

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            input(f"{self.player.name}, нажмите Enter, чтобы атаковать!")
            damage = self.player.attack(self.computer)
            print(f"{self.player.name} атакует {self.computer.name} и наносит {damage} урона!")
            print(f"{self.computer.name} осталось здоровья: {self.computer.health}\n")

            if not self.computer.is_alive():
                print(f"{self.computer.name} был повержен! Поздравляем, {self.player.name}, вы победили!")
                break

            # Ход компьютера
            damage = self.computer.attack(self.player)
            print(f"{self.computer.name} атакует {self.player.name} и наносит {damage} урона!")
            print(f"{self.player.name} осталось здоровья: {self.player.health}\n")

            if not self.player.is_alive():
                print(f"{self.player.name} был повержен! Вы проиграли!")


if __name__ == "__main__":
    game = Game()
    game.start()