import sqlite3

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
          token TEXT NOT NULL
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
          sell_price FLOAT NOT NULL,
          sell_date TEXT,
          FOREIGN KEY(user_id) REFERENCES user(id),
          FOREIGN KEY(action_id) REFERENCES action(id)
     )              
""")

connection.commit()
connection.close()