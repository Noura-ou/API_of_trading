from fastapi import FastAPI

app = FastAPI()


class UserRegister:
    name: str
    email: str
    password: str
    


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "Bonsoir"}
