from pydantic import BaseModel,EmailStr,Field

class UserCreate(BaseModel):
    email:EmailStr
    password:str =Field(min_length=8)
    
class UserRead(BaseModel):
    id: int
    email: EmailStr
    role: str

    model_config = {"from_attributes": True}
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str