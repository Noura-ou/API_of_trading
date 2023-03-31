import sqlite3
import datetime

connection = sqlite3.connect("bdd.db") # Connect to the database 

cursor = connection.cursor() # Create a cursor to execute SQL commands


# -----------------------------||Create a user table||------------------------------------------------
cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS user(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          email TEXT NOT NULL,
          is_active BOOLEAN NOT NULL,
          password TEXT NOT NULL, 
          token TEXT
     )
""")


# -----------------------------||Create a follow table||------------------------------------------------
cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS follow(
          follower_id INTEGER NOT NULL,
          follow_up_id INTEGER NOT NULL,
          FOREIGN KEY(follower_id) REFERENCES user(id),
          FOREIGN KEY(follow_up_id) REFERENCES user(id)
     )
""")

# -----------------------------||Create a action table||------------------------------------------------
cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS action(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          enterprise TEXT NOT NULL,
          price FLOAT NOT NULL,
          date TEXT NOT NULL
     )
""")


# -----------------------------||Create a order table||------------------------------------------------
cursor.execute("""
     CREATE TABLE IF NOT EXISTS trading(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_id INTEGER NOT NULL,
          action_id INTEGER NOT NULL,
          buy_price FLOAT NOT NULL,
          buy_date TEXT,
          sell_price FLOAT,
          sell_date TEXT,
          FOREIGN KEY(user_id) REFERENCES user(id),
          FOREIGN KEY(action_id) REFERENCES action(id)
     )              
""")
               

def insert_data(data_list):
    conn = sqlite3.connect('bdd.db')
    c = conn.cursor()
    c.executemany('INSERT INTO action VALUES (NULL,?,?,?)', data_list)
    conn.commit()
    conn.close()

data_list = [
    ('IBM', 48552.4, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")),
    ('Facebook', 418552.4, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")),
    ('Apple', 248552.4, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")),
    ('Deloite', 448552.4, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")),
    ('Telecom', 4858248552.4, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")),
    ('Yeh', 51248552.4, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")),
    ('FERG', 418552.4, datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
]
insert_data(data_list)


connection.commit()
connection.close()