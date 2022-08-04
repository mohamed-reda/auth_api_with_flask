import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

# do it
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(create_table)

user = (1,'Mo','pass')

insert_query = 'INSERT INTO users VALUES(?,?,?)'

cursor.execute(insert_query,user)
users = [(2,'Mo','pass'),(3,'Mo2','pass2')]


cursor.executemany(insert_query,users)

select_query = 'SELECT * FROM USERS'

for row in cursor.execute(select_query):
    print(row)
# save
connection.commit()
connection.close()
