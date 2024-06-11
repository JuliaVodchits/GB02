class User():
    def __init__(self, user_id, first_name):
        self.first_name = first_name
        self.__user_id = user_id
        self.__role = "user"

    def get_user_id(self):
        return self.__user_id

    def get_user_role(self):
        return self.__role

    def view_user_info(self):
        print(f"Пользователь ID: {self.__user_id}, Имя {self.first_name}")

class Admin(User):
    def __init__(self, user_id, first_name, level):
        super().__init__(user_id, first_name)
        self.__role="admin"
        self.level=level

    def view_user_info(self):
        print(f"Администратор ID: {self.get_user_id()}, Имя {self.first_name}, Уровень доступа: {self.level}")

    def add_user(self, user):
        users.append(user)
        if user.get_user_role() == "user":
            print(f"Добавлен пользователь {user.first_name}")
        else:
            print(f"Добавлен администратор {user.first_name} с уровнем доступа {user.level}")

    def remove_user(self, user_to_remove):
        if user_to_remove.get_user_role() == "user":
            print(f"Удален пользователь {user_to_remove.first_name}")
        else:
            print(f"Удален администратор {user_to_remove.first_name} с уровнем доступа {user_to_remove.level}")
        if user_to_remove in users:
            users.remove(user_to_remove)


users = []

admin1 = Admin(first_name="Иван", level=1, user_id="A1")
user1 = User(first_name="Петр", user_id="U1")
user2 = User(first_name="Семен", user_id="U2")
admin1.add_user(admin1)
admin1.add_user(user1)
admin1.add_user(user2)

admin1.remove_user(user2)

for user in users:
    user.view_user_info()

