from fastapi import Depends , APIRouter, HTTPException ,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import database, schemas, auth, models

router=APIRouter(prefix="/user", tags=["user"])

@router.post("/register", response_model=schemas.UserOut)
def register(user:schemas.UserCreate, db:Session=Depends(database.get_db)):
    db_user=db.query(models.User).filter(models.User.username == user) | (models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400 , detail="User or email already registrated")
    hashed_password=auth.get_password_hash(user.password)
    db_user=models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login", response_model=schemas.Token)
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=auth.authenticate_user(db, form_data.username,form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",  
        )
    access_token=auth.create_access_token(data={"sub":user.username})
    return {"access_token":access_token,"token_type":"bearer"}

@router.get("/me",response_model=schemas.UserOut)
def get_me(current_user:models.User=Depends(auth.get_current_user)):
    return current_user