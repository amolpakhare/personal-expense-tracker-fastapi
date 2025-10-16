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
    class Config:
        populate_by_name = True
        orm_mode = True
        from_attributes=True


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class UserUpdateSchema(UserBaseSchema):
    updated_at: datetime
    hashed_password: Optional[str]=None

class UserResponseSchema(UserBaseSchema):
    updated_at: Optional[datetime]=None
    deleted_at: Optional[datetime]=None
    user_id:int
    class Config:
        from_attributes = True
        populate_by_name = True

class UserRequestSchemaByUserID(BaseModel):
    email: EmailStr
    password: str

class DeleteUserSchemaByUserID(BaseModel):
    user_id:int
    deleted_at: Optional[datetime]=None
    email: EmailStr
    password: str