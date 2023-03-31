import sqlite3
import datetime

# -----------------------------||Create a new user||------------------------------------------------
def create_user(name, email, password, token):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO user(name, email, password, token, is_active)
        VALUES(?,?,?,?,?)
    """, (name, email, password, token, True))
    connection.commit()
    connection.close()

    return cursor.lastrowid


# -----------------------------||Create a search by email||------------------------------------------------
def get_user_by_email(email, password):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM user WHERE email=? AND password=?
    """, (email, password))
    return cursor.fetchall()

# -----------------------------||Update Token||------------------------------------------------

def update_token(id, token:str)->None:
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
                    UPDATE user
                        SET token = ?
                        WHERE id=?
                    """,(token, id))
    connection.commit()
    connection.close()

# -----------------------------||Create action||------------------------------------------------
def create_action(enterprise, price, date):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO action(enterprise, price, date)
        VALUES(?,?,?)
    """, (enterprise, price, date))
    connection.commit()
    connection.close()
    
    return cursor.lastrowid


# -----------------------------||Search action by enterprise name||---------------------------------------
def get_action_by_enterprise(enterprise):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM action WHERE enterprise = ?
    """, (enterprise,))
    return cursor.fetchall()


# -----------------------------||Voir la liste des actions disponibles||----------------------------------
def get_actions():
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM action
    """)
    return cursor.fetchall()

#print(get_actions())


# -----------------------------||Voir ses actions||----------------------------------
def voir_mes_actions(user_id):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM trading WHERE user_id = ?
    """,(user_id,))
    return cursor.fetchall()

#print(voir_mes_actions())

# -----------------------------||Voir les actions des personnes que l'on suit||----------------------------------

def voir_actions_follow(follow_up_id):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute(""" 
        SELECT * FROM trading
        INNER JOIN user ON trading.user_id = user.id
        INNER JOIN follow ON user.id = follow.follower_id AND follow.follow_up_id = ?
    """,(follow_up_id,))
    return cursor.fetchall()


#print(voir_actions_follow(1))


# -----------------------------||Changer la valeur d'une action $$$$$||----------------------------------
def modifie_action(id_action:int, price:float, enterprise:str) -> None :
        connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données
        curseur = connexion.cursor() 

        curseur.execute("""
            UPDATE action 
            SET price = ?, enterprise = ?
            WHERE id = ?
            """,(price, enterprise, id_action))
        
        connexion.commit()
        connexion.close()

#modifie_action("5", "66666666.6666", "tets")

# -----------------------------||Supprimer une Action $$$$$||----------------------------------
def supprimer_action(id : int) -> None :
        connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données
        curseur = connexion.cursor() 

        curseur.execute("""
                 DELETE FROM action 
                 WHERE id = ?
                 """,(id,))
           
        connexion.commit()
        connexion.close()

#supprimer_action("7")

# -----------------------------||Supprimer un user $$$$$||----------------------------------
def supprimer_user(email : str) -> None :
        connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données
        curseur = connexion.cursor() 

        curseur.execute("""
                 DELETE FROM user 
                 WHERE email = ?
                 """,(email,))
           
        connexion.commit()
        connexion.close()

#supprimer_user("gshjddsdk")



# -----------------------------||Modifier un Utilisateur (Email, JWT, Password) ||----------------------------------
def modifie_mail_user(id_user : int, email : str) -> None :
        connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données
        curseur = connexion.cursor() 

        curseur.execute("""
            UPDATE user 
            SET email = ?
            WHERE id = ?
            """,(email, id_user))
        
        connexion.commit()
        connexion.close()

#modifie_mail_user("1", "ami23@gmail.com")

def modifie_jwt_user(id_user : int, token : str) -> None :
        connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données
        curseur = connexion.cursor() 

        curseur.execute("""
            UPDATE user 
            SET token = ?
            WHERE id = ?
            """,(token, id_user))
        
        connexion.commit()
        connexion.close()

#modifie_jwt_user("1", "")

def modifie_mdp_user(id_user : int, password : str) -> None :
        connexion = sqlite3.connect("bdd.db")   #Se connecter à la base de données
        curseur = connexion.cursor() 

        curseur.execute("""
            UPDATE user 
            SET password = ?
            WHERE id = ?
            """,(password, id_user))
        
        connexion.commit()
        connexion.close()

#modifie_mdp_user("1", "")

# -----------------------------||Follow user||-------------------------------------------------
def follow_user(follower_id, follow_up_id):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO follow(follower_id, follow_up_id)
        VALUES(?,?)
    """, (follower_id, follow_up_id))
    connection.commit()
    connection.close()
    
    return cursor.lastrowid


# -----------------------------||Allow trading for user||------------------------------------------------
def trading_user(user_id, action_id, buy_price, buy_date, sell_price, sell_date):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO trading(user_id, action_id, buy_price, buy_date, sell_price, sell_date)
        VALUES(?,?,?,?,?,?)
    """, (user_id, action_id, buy_price, buy_date, sell_price, sell_date))
    connection.commit()
    connection.close()
    
    return cursor.lastrowid