from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from .database import Base
from pydantic import EmailStr


class Post(Base):
    __tablename__ = "posts"
    id=Column(Integer, primary_key=True, nullable=False)
    title=Column(String, nullable=False)
    content=Column(String, nullable=False)
    published=Column(Boolean, server_default='TRUE', nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id=Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner=relationship("User")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class User(Base):
    __tablename__ = "users"
    id=Column(Integer, primary_key=True, nullable=False)
    email=Column(String, nullable=False, unique=True)
    password=Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Vote(Base):
    __tablename__ = "votes"
    post_id=Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    user_id=Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, nullable=False)

class Comment(Base):
    __tablename__ = "comments"
    id=Column(Integer, primary_key=True, nullable=False)
    comment=Column(String, nullable=False, default="no comments yet")
    post_id=Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    email=Column(String, ForeignKey("users.email", ondelete="CASCADE"), nullable=False)
    user=relationship("User")
    post = relationship("Post", back_populates="comments")