from fastapi import FastAPI
from .routers import task, user
from sqlalchemy.schema import CreateTable


app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
