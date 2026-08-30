from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models, schemas, oauth2
from ..database import get_db
from typing import List, Optional
from app.schemas import PostResponse, CommentOut, PostOut
router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


# def postout(posts):
#     if isinstance(posts, tuple):
#         post, vote_count = posts
#         return schemas.PostOut(Post=post, vote=vote_count)

#     return [schemas.PostOut(Post=post, vote=vote_count) for post, vote_count in posts]


# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostResponse] )
async def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str]= ""):

    posts = (db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
               .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
               .group_by(models.Post.id)
               .filter(models.Post.title.contains(search))
               .limit(limit)
               .offset(skip)
               .all())
    response = []

    for post in posts:
        response.append(
            schemas.PostResponse(
                Post=post[0],   
                comments=[
                    schemas.CommentOut.model_validate(comment)
                    for comment in post[0].comments
                    ],
                votes=post[1]
            )
        )

    return response


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # post = db.query(models.Post).filter(models.Post.id == id).first()

    posts = (db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
                   .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
                   .group_by(models.Post.id).filter(models.Post.id == id).first()
    )
    if posts == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="you do not have the autherization")
    post, votes = posts
    response = schemas.PostResponse(
        Post=post,
        comments=[
            schemas.CommentOut.model_validate(comment)
            for comment in post.comments
        ],
        votes=votes
    )
    return response

@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="you do not have the autherization")
    db.delete(post)
    db.commit()
    return {"message": f"post with id: {id} was deleted successfully"}



@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    new_post = post_query.first()
    if new_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    if new_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="you do not have the autherization")
    post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()
