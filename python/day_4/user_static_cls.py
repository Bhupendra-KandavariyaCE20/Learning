class User:
    usercount = 0 # count of users
    def __init__(self, username):
        self.username = username
        User.usercount+=1

    @classmethod
    def from_json(cls, json_data:dict):
        return cls(username = json_data['user_name'])

    @staticmethod
    def is_valid_username(username)->bool:
        return len(username)>3


user_bk =  User("bhupendra")
json_data = {"user_name":"alice", "email":"alice@gmail.com"}
user_alic = User.from_json(json_data)
print(user_alic.usercount)
