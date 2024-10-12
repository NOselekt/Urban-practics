from fastapi import APIRouter
from Rep.Module_17.module_17_1.app.backend.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .user import User

router = APIRouter(prefix="/task", tags=["task"])

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    slug = Column(String, index=True, unique=True)

    user = relationship("User", back_populates="tasks")



@router.get("/")
async def all_tasks(): ...

@router.get("/task_id")
async def task_by_id(): ...

@router.post("/create")
async def create_task(): ...

@router.put("/update")
async def update_task(): ...

@router.delete("/delete")
async def delete_task(): ...