from sqlalchemy import String, Column,Integer,Text,ForeignKey,DateTime,Boolean
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    email=Column(String,unique=True,index=True)
    hashed_password=Column(String)
    created_at=Column(DateTime,default=datetime.utcnow)

    task=relationship("Task",back_populates="user",cascade="all, delete-orphan")

class Task(Base):
    __tablename__="tasks"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,unique=False,nullable=False)
    description=Column(String,nullable=True)
    is_completed=Column(Boolean,default=False)
    priority=Column(Integer,default=2)
    due_date=Column(DateTime,nullable=True)
    created_at=Column(DateTime,default=datetime.utcnow)
    user_id=Column(Integer,ForeignKey("user.id"),nullable=False)

    user=relationship("User",back_populates="tasks")
