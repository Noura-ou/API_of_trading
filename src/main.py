from fastapi import FastAPI
import sql_crud_test
from fastapi import FastAPI, HTTPException, Request, Depends
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import hashlib
import os


SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

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
    mdp:str

class UserLogin(BaseModel):
    email:str
    mdp:str
    
class Action(BaseModel):
    titre: str
    contenu: str
    auteur_id: int

# Début des endpoints
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "Bonsoir"}


@app.post("/api/auth/inscription")
async def inscription(user:UserRegister):
    if len(sql_crud_test.get_user_by_email(user.email)) > 0:
        raise HTTPException(status_code=403, detail="L'email fourni possède déjà un compte")
    else:
        id_user = sql_crud_test.create_user(user.nom, user.email, hasher_mdp(user.mdp), None)
        token = jwt.encode({
            "email" : user.email,
            "mdp" : user.mdp,
            "id" : id_user
        }, SECRET_KEY, algorithm=ALGORITHM)
        sql_crud_test.update_token(id_user, token)
        return {"token" : token}



@app.post("/api/action")
async def create_action(action : Action):
   try:
        create_action(action.titre, action.contenu, action.auteur_id)
        return {"message": "Action created successfully"}
   except Exception as e:
        raise HTTPException(status_code=401, detail="l'action n'a pas était crée")

