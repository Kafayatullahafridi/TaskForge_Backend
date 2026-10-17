from fastapi.security import OAuth2PasswordBearer
import jwt
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.db.session import get_db
from app.models.users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")