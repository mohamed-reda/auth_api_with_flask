from hmac import compare_digest
from auth.user import User

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
    User(3, 'Mohamed@gmail.com', '12345678'),
]

# username_mapping = {
#     'id': 3,
#     'username': 'Mohamed@gmail.com',
#     'password': '12345678'
# }

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
