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




connection.commit()
connection.close()