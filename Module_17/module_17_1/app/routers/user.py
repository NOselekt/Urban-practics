from fastapi import APIRouter
from app.backend.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


router = APIRouter(prefix="/user", tags=["user"])


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, index=True, unique=True)

    tasks = relationship("Task", back_populates="user")


@router.get("/")
async def all_users(): ...

@router.get("/user_id")
async def user_by_id(): ...

@router.post("/create")
async def create_user(): ...

@router.put("/update")
async def update_user(): ...

@router.delete("/delete")
async def delete_user(): ...