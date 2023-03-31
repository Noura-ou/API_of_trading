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

#print(get_action_by_enterprise("Facebook"))

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
def voir_mes_actions(user_id :int):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM trading WHERE user_id = ?
    """,(user_id,))
    return cursor.fetchall()

#print(voir_mes_actions(2))

# -----------------------------||Voir les actions des personnes que l'on suit||----------------------------------

def voir_actions_follow(id_user):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute(""" 
        SELECT trading.user_id,trading.action_id, trading.buy_price, trading.buy_date, trading.sell_price, trading.sell_date FROM trading
        INNER JOIN user ON trading.user_id = user.id
        INNER JOIN follow ON user.id = follow.follower_id AND follow.follow_up_id = ?
    """,(id_user,))
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

#follow_user(2,4)


def read_follower(follower_id):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM follow WHERE follower_id = ?
        """, (follower_id,))
    
    result = cursor.fetchall()   

    connection.close()
    
    return result

#print(read_follower(1))

def read_follow_up(follow_up_id):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM follow WHERE follow_up_id = ?
        """, (follow_up_id,))
    
    result = cursor.fetchall()
    
    connection.close()
    
    return result


def update_follow(follower_id, follow_up_id):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE follow
        SET follow_up_id = ?
        WHERE follower_id = ?
        """, (follow_up_id, follower_id))
    
    connection.commit()
    connection.close()
    
    return cursor.lastrowid


# -----------------------------||Allow trading for user||------------------------------------------------
def buy_action(user_id: int, action_id: int, buy_date: str, buy_price: float, sell_price : float, sell_date : str):
    connection = sqlite3.connect('bdd.db')
    cursor = connection.cursor()
    cursor.execute("""
            INSERT INTO trading (user_id, action_id, buy_date, buy_price,sell_price, sell_date) 
            VALUES (?,?,?,?,NULL,NULL)""",
            (user_id, action_id, buy_date, buy_price))
    connection.commit()
    connection.close()


buy_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

#buy_action(4, 5, buy_date,11115924.3788,None, None)


def sell_action(action_id: int, sell_price: float, sell_date: str):
    connection = sqlite3.connect('bdd.db')
    cursor = connection.cursor()
    cursor.execute("""
            UPDATE trading 
            SET sell_price = ?, sell_date = ? 
            WHERE id = ?""", (sell_price, sell_date, action_id))
    connection.commit()
    connection.close()

#sell_action(3,6857.35,datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))