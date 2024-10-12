from app.backend.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .task import Task


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
