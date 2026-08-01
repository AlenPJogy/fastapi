from fastapi import Body, status, HTTPException, Depends, APIRouter
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session


router = APIRouter( prefix = "/comments", tags= ['comment'])

@router.post("/", status_code=status.HTTP_201_CREATED)
def comment(comment: schemas.CommentBase, db: Session = Depends(database.get_db),  current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == comment.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {comment.post_id} not found")
    new_comment = models.Comment(comment=comment.comment, post_id=comment.post_id, email=current_user.email)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return {"message": "successfully added comment", "comment": new_comment}
