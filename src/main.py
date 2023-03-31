from fastapi import FastAPI
import sql_crud_test
from fastapi import FastAPI, HTTPException, Request, Depends
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import hashlib


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
        token = jwt.encode({
            "email" : user.email,
            "mdp" : user.password,
            "id" : id_user
        }, SECRET_KEY, algorithm=ALGORITHM)
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
async def list_action(user_id: int):
    actions = sql_crud_test.voir_mes_actions(user_id)
    return [{"action_id": row[1], "quantite": row[2], "prix": row[3],"price": row[4], "price": row[5],"oko": row[6]} for row in actions]