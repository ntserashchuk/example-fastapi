from typing import List, Optional
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from .. import models, schemas, oauth2

router = APIRouter(
    prefix="/posts",
    tags=['POSTS']
)

from .. import models, schemas

from ..database import get_db
from sqlalchemy.orm import Session

@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user), 
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    # results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
    #     models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id)
    
    # print(results.first().Post.owner_id)

    return posts

@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    print(post.owner_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} is not found")
    return post





@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    new_post = models.Post(**post.model_dump())

    new_post.owner_id = current_user.id

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post_to_delete = post_query.first()
    if post_to_delete == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    
    if post_to_delete.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"post with id {id} is not allowed to delete by current user")

    post_query.delete()
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post_db = post_query.first()

    if post_db == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    if post_db.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"post with id {id} is not allowed to update by current user")
    
    post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()

    return post_query.first()
