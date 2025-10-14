from fastapi import APIRouter,Depends
from Eusers.schema import (UserRegisterationSchema, UserUpdateSchema, UserResponseSchema,UserRequestSchemaByUserID,UserLoginSchema,DeleteUserSchemaByUserID)
from Eusers.service import (create_register_user, update_user_details,get_user_by_id,delete_user_by_userid,get_all_users)
from database import get_db
from sqlalchemy.orm import Session

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.post("/register",response_model=UserRegisterationSchema)
def register_user(user:UserRegisterationSchema,db:Session = Depends(get_db)):
    return create_register_user(db,user)  

@user_router.put("/update/{user_email}/{user_password}",response_model=UserUpdateSchema)
def update_user(user_email:str,user_password:str,update_details:UserUpdateSchema,db:Session = Depends(get_db)):
    return update_user_details(user_email,user_password,update_details,db) 

@user_router.get("/login/{email}/{password}")
def login_user(email:str,password:str,db:Session = Depends(get_db)):
    return get_user_by_id(email,password,db)

@user_router.delete("/delete/user/{email}/{password}")
def delete_user(data : DeleteUserSchemaByUserID,db:Session = Depends(get_db)):
    return delete_user_by_userid(data,db)

@user_router.get("/all")
def all_users(db:Session = Depends(get_db)):
    return get_all_users(db)
