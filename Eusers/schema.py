from pydantic import BaseModel, EmailStr
from typing import Optional  
from datetime import datetime

class UserBaseSchema(BaseModel):
    nickname: Optional[str]=None
    email: Optional[EmailStr]=None
    mobile_no: Optional[int]=None
    full_name: Optional[str]=None
    is_active: Optional[int]=1
    created_at: Optional[datetime]=None

class UserRegisterationSchema(UserBaseSchema):
    hashed_password: str

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class UserUpdateSchema(UserBaseSchema):
    updated_at: datetime
    hashed_password: Optional[str]=None

class UserResponseSchema(UserBaseSchema):
    User_id:int
    class Config:
        orm_mode = True

class UserRequestSchemaByUserID(BaseModel):
    email: EmailStr
    password: str

class DeleteUserSchemaByUserID(BaseModel):
    User_id:int
    deleted_at: Optional[datetime]=None
    email: EmailStr
    password: str