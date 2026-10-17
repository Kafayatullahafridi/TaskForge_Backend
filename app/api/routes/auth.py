
from sqlalchemy import select
from app.models.users import User
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password, create_access_token
from app.db.session import get_db
from app.schemas.users import UserCreate, UserRead, LoginRequest
router  = APIRouter(prefix='/auth',tags=['auth'])

@router.post('/register',status_code=201,response_model=UserRead)
def register(user_in:UserCreate, db :Session = Depends(get_db)):
    existing = db.scalar(select(User).where(User.email == user_in.email))
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")
    new_user = User(email=user_in.email, hashed_password=hash_password(user_in.password))
    db.add(new_user)
    db.commit()
    return new_user
 
 
@router.post('/token')
def login(login_in:LoginRequest,db:Session=Depends(get_db)):
   user = db.scalar(select(User).where(User.email==login_in.email) )
   if user is None or not verify_password(login_in.password, user.hashed_password):
       raise HTTPException(status_code=401,detail='invalid email or password')
   token = create_access_token(user.id)
   return {"access_token":token, "token_type":"bearer"}