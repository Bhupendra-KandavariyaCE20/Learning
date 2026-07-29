class User:

    def __init__(self, username: str, email):
        self.username = username
        self.email = email

    def send_email(self, message: str):
        print(f"Sending to {self.email} : {message}")

user1 = User("alice", "alice@gmail.com")
user1.send_email("Hi how are you")

