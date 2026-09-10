from fastapi import Body, status, HTTPException, Depends, APIRouter
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session


router = APIRouter(prefix="/comments", tags=['comment'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.CommentOut)
def comment(comment: schemas.CommentBase, db: Session = Depends(database.get_db),  current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(
        models.Post.id == comment.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {comment.post_id} not found")
    new_comment = models.Comment(
        comment=comment.comment, post_id=comment.post_id, email=current_user.email)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    comment_query = db.query(models.Comment).filter(models.Comment.id == id)
    comment = comment_query.first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Comment with id {id} not found")
    if comment.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    db.delete(comment)
    db.commit()
    return {"message": "Comment deleted successfully"}
