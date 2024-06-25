from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from src.db import crud
from src.db.schemas import User, UserCreate
from src.db.database import get_db
from src.utils.auth import create_session_token, authenticate_user


router = APIRouter()

@router.post("/login/")
async def login(response: Response,
                form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_db)):
    
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
            
    session_token = create_session_token(user.user_name)
    response.set_cookie(key="token", value=session_token, httponly=True)
    
    return {"success": "you are logged in"}

@router.post("/sign_up/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    
    db_user = crud.get_user(db, user_name=user.user_name)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    return crud.create_user(db=db, user=user)
