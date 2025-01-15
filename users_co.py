class User():

    def __init__(self, id, name):
        self.__id = id # приватный атрибут
        self.__name = name # приватный атрибут
        self.__dostup = 'user' # Уровень доступа для обычных сотрудников

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dostup(self):
        return self.__dostup


class Admin(User):

    def __init__(self, id, name):
        super().__init__(id,name)
        self.__dostup = 'admin' #приватный доступ
        self.__users = [] #приватный атрибут список пользователей

    def get_access(self):
        return self.__dostup



    def add_user(self,user):
        if user in self.__users:
            print(f"Такой пользователь  {user.get_name()} уже существует")

        else:
            self.__users.append(user)
            print(f"Пользователь  {user.get_name()}, регистрационный номер {user.get_id()}- добавлен")

    def remove_user(self,user):
        if user not in self.__users:
            print(f"Такого пользователя {user.get_name()} не существует")

        else:
            self.__users.remove(user)
            print(f"Пользователь {user.get_id()}, регистрационный номер {user.get_id()}- удален")


user1 = User(124, "Ivan")
user2 = User(254, "Nata")
user3 = Admin(147, "Stas")
user4 = User(365, "Ivan")

user3.add_user(user1)
user3.add_user(user2)
user3.remove_user(user4)
user3.remove_user(user1)


