from fastapi import FastAPI, HTTPException
from database import SessionLocal, get_db
from models import Post
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()


from schemas import CreatePost, PostResponse

@app.post("/posts", response_model=PostResponse)
def create_post(
    post :  CreatePost,
    db: Session = Depends(get_db)
):
    new_post = Post(
        content = post.content,
        author = 'anonymous'
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts", response_model=List[PostResponse])
def get_posts( db: Session = Depends(get_db)):
    return db.query(Post).all()

@app.get("/posts/{post_id}")
def get_post(post_id: int,  db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first() 

    if post is None:
        raise HTTPException(
            status_code=404,
            detail='Post not found'
        )
    return post

@app.delete("/posts/{post_id}")
def delete_post(post_id: int,  db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    
    if post is None:
        raise HTTPException(
            status_code=404,
            detail='Post not found'
        )
    db.delete(post)
    db.commit()
    return {"message" : "Post deleted successfully"}

@app.put("/posts/{post_id}")
def update_post(
    post_id: int,
    post_update: CreatePost,  
    db: Session = Depends(get_db)
):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(
            status_code = 404,
            detail = 'Post not found'
        )
    post.content = post_update.content
    db.commit()
    return post