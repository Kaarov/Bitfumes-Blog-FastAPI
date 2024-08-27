from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from blog import schemas, database, models
from blog.hashing import Hash

router = APIRouter(
    tags=["Authentication"],
)


@router.post("/login")
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")
    # generate a jwt token and return
    return user
