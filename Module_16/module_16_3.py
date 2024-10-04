from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def welcome() -> str:
    return "Main page"

@app.get("/users")
async def get_dict() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: str = Path(min_length=5, max_length=20, description="Enter username", example="admin"),
                   age: int = Path(ge=18, le=120, description="Enter age", example="23")) -> str:
    last_index = max(users, key=int)
    users[last_index] = f"Имя: {username}, возраст: {age}"
    return f"User №{last_index} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(id_: str = Path(ge=1, le=100, description="Enter User ID", example=1),
                      username: int = Path(min_length=5, max_length=20, description="Enter username", example="admin"),
                      age: int = Path(ge=18, le=120, description="Enter age", example="23")) -> str:
    users[id_] = f"Имя: {username}, возраст: {age}"
    return f"The user №{id_} is registered"

@app.delete("/user/{user_id}")
async def delete_user(id_: str = Path(ge=1, le=100, description="Enter User ID", example=1)) -> str:
    users.pop(id_)
    return f"The user №{id_} is deleted"