import sqlite3
from hmac import compare_digest
from auth.user import User


# 
# users = [
#     User(1, 'user1', 'abcxyz'),
#     User(2, 'user2', 'abcxyz'),
#     User(3, 'Mohamed@gmail.com', '12345678'),
# ]


def authenticate(username, password):
    user = User.find_by_username(username=username)

    # if user is None:
    #     connection = sqlite3.connect("data.db")
    #     cursor = connection.cursor()
    #     insert_query = 'INSERT INTO users VALUES(?,?,?)'
    #     r_user = User(id=2323, username=username, password=password)
    #     n_user = (2323, username, password)
    #     # do it
    #     cursor.execute(insert_query, n_user)
    #     # save
    #     connection.commit()
    #     connection.close()
    #     return r_user
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']

    return User.find_by_id(user_id)
