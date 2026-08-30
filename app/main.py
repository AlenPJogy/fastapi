from fastapi import Body, FastAPI

from . import models
from .database import engine
from .routers import post, user, auth, vote, comment
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app =FastAPI()

origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(comment.router)


@app.get("/")
async def root():
    return {"message": "hello everynyan"}




































# @app.get("/posts", response_model=List[schemas.Post])
# async def get_posts(db: Session = Depends(get_db)):
#     # cursor.execute("""SELECT * FROM posts""")
#     # posts= cursor.fetchall()
#     posts=db.query(models.Post).all()
#     return posts


# @app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""", (post.title,post.content,post.published))
#     # new_post=cursor.fetchone()
#     # conn.commit()

#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post


# @app.get("/posts/{id}", response_model=schemas.Post)
# def get_post(id: int, db: Session = Depends(get_db)): # response: Response):
#     # cursor.execute("""SELECT * FROM posts WHERE id=%s""",(id,))
#     # post=cursor.fetchone()
#     # post = find_post(id)
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": f"post with id: {id} was not found"}
#     return post


# def find_index(id):
#     for i in my_posts:
#         if i['id']==id:
#             return my_posts.index(i)

# @app.delete("/posts/{id}")
# def delete_post(id: int, db: Session = Depends(get_db)):
#     # index = find_index(id)
#     # cursor.execute("""DELETE FROM posts WHERE id=%s RETURNING *""",(id,))
#     # deleted_post=cursor.fetchone()
#     # conn.commit()
#     deleted_post = db.query(models.Post).filter(models.Post.id == id).first()

#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#     # my_posts.pop(index)
#     db.delete(deleted_post)
#     db.commit()
#     return {"message": f"post with id: {id} was deleted successfully"}

# @app.put("/posts/{id}", response_model=schemas.Post)
# def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # print(post)
#     # index = find_index(id)
#     # cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *""", (post.title, post.content, post.published, id))
#     # updated_post = cursor.fetchone()
#     # conn.commit()
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     new_post = post_query.first()

#     if new_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#     # post_dict= post.model_dump()
#     # post_dict['id'] = id
#     # my_posts[index]=post_dict
#     post_query.update(post.model_dump(), synchronize_session=False)
#     db.commit()
#     return post_query.first()

