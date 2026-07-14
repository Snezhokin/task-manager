from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username:str
    email:EmailStr

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    username:str
    email:EmailStr
    created_at:datetime

    class Config:
        from_attributes=True

class TaskBase(BaseModel):
    title:str
    description:Optional[str]=None
    is_completed:bool=False
    priority:int=2
    due_date:datetime

class TaskCreate(BaseModel):
    title:str
    description:Optional[str]=None
    is_completed:bool
    priority:int
    due_date:datetime

class TaskUpdate(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    is_completed:Optional[bool]=None
    priority:Optional[int]=None
    due_date:Optional[datetime]=None

class TaskOut(BaseModel):
    id:int
    title:str
    description:Optional[str]=None
    is_completed:bool
    priority:int
    due_date:datetime
    create_at:datetime
    user_id:int

    class Config:
        from_attributes=True

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:Optional[str]=None

