from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

users = {1: 'Имя: Example, возраст: 18'}

@app.get("/")
async def welcome() -> str:
    return "Main page"

@app.get("/users")
async def get_dict() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: str = Path(min_length=5, max_length=20, description="Enter username", example="executor"),
                   age: int = Path(ge=18, le=120, description="Enter age", example="23")) -> str:
    try:
        last_index = max(users, key=int)
    except ValueError:
        last_index = 1
    users[last_index] = f"Имя: {username}, возраст: {age}"
    return f"User №{last_index} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int = Path(gt=1, le=100, description="Enter User ID", example=2),
                      username: str = Path(min_length=5, max_length=20, description="Enter username", example="executor"),
                      age: int = Path(ge=18, le=120, description="Enter age", example=23)) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user №{user_id} is registered"

@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=2)) -> str:
    try:
        users.pop(user_id)
        return f"The user №{user_id} is deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="The dictionary's already empty")