import sqlite3
from sql_creer import connection 


cursor = connection.cursor()



# -----------------------------||Create a user table||------------------------------------------------
def create_user(name, email, password, token):
    cursor.execute("""
        INSERT INTO user(name, email, password, token)
        VALUES(?,?,?,?)
    """, (name, email, password, token))
    connection.commit()
    connection.close()
    
    return cursor.lastrowid


# -----------------------------||Create a search by email||------------------------------------------------
def get_user_by_email(email):
    cursor.execute("""
        SELECT * FROM user WHERE email = ?
    """, (email,))
    return cursor.fetchone()