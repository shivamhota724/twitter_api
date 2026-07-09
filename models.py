from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)