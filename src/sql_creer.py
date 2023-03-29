import sqlite3

connection = sqlite3.connect("bdd.db")   #Se connecter à la base de données

cursor = connection.cursor() #SQL.sh pour apprender SQL

cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
            )
""")

cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS action(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            enterprise TEXT NOT NULL,
            price TEXT NOT NULL
            )
""")


cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS following(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(id)
            )
""")

cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS user_actions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(action_id) REFERENCES action(id)
            )
""")

cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS sell_order(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action_id INTEGER,
            sell_date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(action_id) REFERENCES action(id)
            )
""")

cursor.execute(""" 
       CREATE TABLE IF NOT EXISTS buyed_order(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action_id INTEGER,
            buyed_date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(action_id) REFERENCES action(id)
            )
""")


connection.commit()
connection.close()