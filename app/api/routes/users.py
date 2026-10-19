from fastapi import APIRouter, Depends

from app.api.deps import get_current_user
from app.models.users import User
from app.schemas.users import UserRead

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserRead)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user