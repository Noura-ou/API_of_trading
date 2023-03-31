import sqlite3
from sql_creer import connection 


cursor = connection.cursor()



# -----------------------------||Create an Action ||------------------------------------------------
def create_action(date, entreprise, price):
    cursor.execute("""
        INSERT INTO action(date, )
        VALUES(?,?,?)
    """, (date, entreprise, price))
    connection.commit()
    connection.close()
    
    return cursor.lastrowid