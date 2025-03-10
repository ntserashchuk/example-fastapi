
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

class PostOut(PostBase):
    # Post: Post
    votes: int

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)