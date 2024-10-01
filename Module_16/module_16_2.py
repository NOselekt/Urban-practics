from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def welcome() -> str:
    return "Main page"

@app.get("/user/admin")
async def welcome_admin() -> str:
    return "You logged in as an administrator"

@app.get("/user/{id_}")
async def welcome_user(id_: int = Path(ge=1, le=100, description="Enter User ID", example=1)) -> str:
    return f"You logged in as user №{id_}"

@app.get("/user/{username}/{age}")
async def user_info(username: str = Path(min_length=5, max_length=20, description="Enter username", example="admin"),
                    age: int = Path(ge=18, le=120, description="Enter age",example="23")) -> str:
    return f"User's inforamtion: username: {username}, age: {age}"