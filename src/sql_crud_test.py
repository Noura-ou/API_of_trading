import sqlite3


# -----------------------------||Create a new user||------------------------------------------------
def create_user(name, email, password, token=None):
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
def get_user_by_email(email):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM user WHERE email = ?
    """, (email,))
    return cursor.fetchall()

# -----------------------------||Update Token||------------------------------------------------

def update_token(id, token:str)->None:
    connexion = sqlite3.connect("bdd.db")
    curseur = connexion.cursor()
    curseur.execute("""
                    UPDATE utilisateur
                        SET jwt = ?
                        WHERE id=?
                    """,(token, id))
    connexion.commit()
    connexion.close()

# -----------------------------||Create action||------------------------------------------------
def create_action(enterprise, price):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO action(enterprise, price)
        VALUES(?,?)
    """, (enterprise, price))
    connection.commit()
    connection.close()
    
    return cursor.lastrowid


# -----------------------------||Search action by enterprise name||------------------------------------------------
def get_action_by_enterprise(enterprise):
    connection = sqlite3.connect("bdd.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM action WHERE enterprise = ?
    """, (enterprise,))
    return cursor.fetchone()


# -----------------------------||Follow user||------------------------------------------------
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