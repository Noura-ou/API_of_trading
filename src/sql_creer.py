import sqlite3

connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données

curseur = connexion.cursor() #SQL.sh pour apprender SQL

curseur.execute(""" 
       CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            mdp TEXT NOT NULL
            )

""")

connexion.commit()