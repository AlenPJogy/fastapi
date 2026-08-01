from datetime import datetime
from typing import Annotated, List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    created_at: datetime

class UserCommentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: str


class Post(PostBase):

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    comments: List["CommentOut"]= []

class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    Post: Post
    votes: int

class CommentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)


    id: int
    comment: str
    email: UserCommentOut


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
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)]

class CommentBase(BaseModel):
    comment: str
    post_id: int






    
