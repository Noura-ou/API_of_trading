from fastapi import FastAPI
import sqlite3
import sql_crud_test
from fastapi import FastAPI, HTTPException, Request, Depends
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import hashlib
import datetime
import secrets

SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

app = FastAPI()

# Fonctions utiles :
def hasher_mdp(mdp:str) -> str:
    return hashlib.sha256(mdp.encode()).hexdigest()

def decoder_token(token:str)->dict:
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

def verifier_token(req: Request):
    token = req.headers["Authorization"]

# Classes contenu
class UserRegister(BaseModel):
    nom:str
    email:str
    password:str

class UserLogin(BaseModel):
    email:str
    password:str
    
class Action(BaseModel):
    enterprise: str
    price: float
    
class Follower(BaseModel):
    follower_id: int
    follow_up_id: int

class Trade(BaseModel):
    user_id: int
    action_id: int
    buy_price: float
    sell_price: float = None
    buy_date: str = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    sell_date: str = None
    
class Sell(BaseModel):
    action_id: int
    sell_price: float

# Début des endpoints
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "Bonsoir"}


@app.post("/api/auth/inscription")
async def inscription(user:UserRegister):
    if len(sql_crud_test.get_user_by_email(user.email, user.password)) > 0:
        raise HTTPException(status_code=403, detail="L'email fourni possède déjà un compte")
    else:
        id_user = sql_crud_test.create_user(user.nom, user.email, hasher_mdp(user.password), None)
        token = secrets.token_hex(50)
        sql_crud_test.update_token(id_user, token)
        return {"token" : token}


@app.post("/api/auth/login")
async def login_token(user: UserLogin):
    resultat = sql_crud_test.get_user_by_email(user.email, hasher_mdp(user.password))
    if len(resultat) == 0:
        raise HTTPException(status_code=401, detail="Login ou mot de passe invalide")
    else:
        return {"token": resultat[0]}


@app.get("/api/auth/listAction")
async def list_action():
    actions = sql_crud_test.get_actions()
    return [{ "user_id": row[0], "enterprise": row[1],"price": row[2], "date": row[3]} for row in actions]


@app.get("/api/auth/userAction")
async def list_action(user_id: int):
    actions = sql_crud_test.voir_mes_actions(user_id)
    return [{ "user_id": row[1], "action_id": row[2],"buy_price": row[3], "buy_date": row[4],"sell_price": row[5] if row[5] is not None else '', "date_price": row[6] if row[6] is not None else ''} for row in actions]

@app.get("/api/auth/listActionFollow")
async def list_action(user_id: int):
    actions = sql_crud_test.voir_actions_follow(user_id)
    return [{ "user_id": row[0], "action_id": row[1],"buy_price": row[2], "buy_date": row[3], "sell_price": row[4] if row[4] is not None else '', "date_price": row[5] if row[5] is not None else ''} for row in actions]


@app.put("/api/auth/followuser")
async def follow_user_route(follower_id: int, follow_up_id: int):
    sql_crud_test.follow_user(follower_id, follow_up_id)
    return {"message": "Follow added successfully"}



@app.post("/api/auth/trading/buy")
async def buy(trade: Trade):
    buy_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    sql_crud_test.buy_action(trade.user_id, trade.action_id, buy_date, trade.buy_price, None, None)
    return {"message": "Transaction réussie."}


@app.put("/api/auth/trading/sell")
async def sell(sell_data: Sell):
    sell_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    sql_crud_test.sell_action(sell_data.action_id, sell_data.sell_price, sell_date)
    return {"message": f"La transaction {sell_data.action_id} a été vendue."}
