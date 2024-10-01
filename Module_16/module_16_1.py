from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> str:
    return "Main page"

@app.get("/user/admin")
async def welcome() -> str:
    return "You logged in as an administrator"

@app.get("/user/{id_}")
async def welcome(id_ = 0) -> str:
    return f"You logged in as user №{id_}"

@app.get("/user/")
async def welcome(username: str = "admin", age: int = 23) -> str:
    return f"User's inforamtion: username: {username}, age: {age}"