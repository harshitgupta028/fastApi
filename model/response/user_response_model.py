from typing import Optional, List
from pydantic import BaseModel
from pydantic import EmailStr

class UserResponseDeletedModel(BaseModel):
    id: int

class User(BaseModel):
    id: int 
    name: str 
    email: Optional[EmailStr] | None = None

class UserResponseModel(BaseModel):
    user: List[User]