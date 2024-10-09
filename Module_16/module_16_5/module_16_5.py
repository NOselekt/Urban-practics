from fastapi import FastAPI, Path, HTTPException, status, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory="C:/Users/admin/Projects/PracticsUrban/Rep/Module_16/module_16_5/templates")


class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None


users: list[User] = []


@app.get("/")
async def welcome(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get(path="/user/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(request: Request,
                   user_id: int = Path(ge=1, le=100, description="Enter User ID", example=2)) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/{username}/{age}", status_code=status.HTTP_201_CREATED)
async def add_user(username: str = Path(min_length=5, max_length=20, description="Enter username", example="executor"),
                   age: int = Path(ge=18, le=120, description="Enter age", example="23")) -> User:
    new_user = User(id=len(users) + 1, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=2),
                      username: str = Path(min_length=5, max_length=20, description="Enter username",
                                           example="executor"),
                      age: int = Path(ge=18, le=120, description="Enter age", example=23)) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.id = user_id
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", status_code=status.HTTP_302_FOUND)
async def delete_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=2)) -> User:
    try:
        return users.pop(user_id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
