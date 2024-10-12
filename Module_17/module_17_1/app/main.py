from fastapi import FastAPI
from routers import task, user
from sqlalchemy.schema import CreateTable


print(CreateTable(user.User.__table__))
print(CreateTable(task.Task.__table__))

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
