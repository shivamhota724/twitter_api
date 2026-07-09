from fastapi import FastAPI, HTTPException
from database import SessionLocal, get_db
from models import Post, User
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List
from utils import hash, verify
from oauth2 import create_access_token
from oauth2 import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()


from schemas import CreatePost, PostResponse, CreateUser, UserResponse, UserLogin, Token

@app.post("/users", response_model=UserResponse)
def create_user(
    user: CreateUser,
    db: Session = Depends(get_db)
):
    new_user = User(
        email = user.email,
        password = hash(user.password)
    )
    existing_user = db.query(User).filter(User.email == user.email).first()
    
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail='email already exists'
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == user_credentials.username).first()

    if user is None:
        raise HTTPException(
            status_code=403,
            detail="Invalid credentials"
        )

    if not verify(user_credentials.password, user.password):
        raise HTTPException(
        status_code=403,
        detail="Invalid credentials"
    )
    access_token = create_access_token(
        data={"user_id": user.id}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.post("/posts", response_model=PostResponse)
def create_post(
    post :  CreatePost,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_post = Post(
        content = post.content,
        owner_id = current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts", response_model=List[PostResponse])
def get_posts( db: Session = Depends(get_db)):
    return db.query(Post).all()

@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int,  db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first() 

    if post is None:
        raise HTTPException(
            status_code=404,
            detail='Post not found'
        )
    return post

@app.delete("/posts/{post_id}")
def delete_post(
    post_id: int,  
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    post = db.query(Post).filter(Post.id == post_id).first()
    
    if post is None:
        raise HTTPException(
            status_code=404,
            detail='Post not found'
        )
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to perform this action"
        )
    db.delete(post)
    db.commit()
    return {"message" : "Post deleted successfully"}

@app.put("/posts/{post_id}")
def update_post(
    post_id: int,
    post_update: CreatePost,  
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post is None:
        raise HTTPException(
            status_code=404,
            detail='Post not found'
        )
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to perform this action"
        )
    post.content = post_update.content
    db.commit()
    return post