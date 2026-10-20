class User:

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def print_user(self):
        print(f"Name {self.__name} and Email {self.__email}")

user1 = User("bhupendra", "bk@gmail.com")
user1.print_user()

try:
    print(user1.__name)
except Exception as e:
    print(e)
