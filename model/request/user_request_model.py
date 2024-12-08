from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional

class UserRequestModel(BaseModel):
    name: str
    email: Optional[EmailStr] | None = None

class UserRequestUpdateModel(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] | None = None