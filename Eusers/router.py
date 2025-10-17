# from fastapi import APIRouter,Depends
# from Eusers.schema import (UserRegisterationSchema, UserUpdateSchema, UserResponseSchema,UserRequestSchemaByUserID,UserLoginSchema,DeleteUserSchemaByUserID)
# from Eusers.service import (create_register_user, update_user_details,get_user_by_id,delete_user_by_userid,get_all_users)
# from database import get_db
# from sqlalchemy.orm import Session

# user_router = APIRouter(
#     prefix="/users",
#     tags=["users"]
# )

# @user_router.post("/register",response_model=UserRegisterationSchema)
# def register_user(user:UserRegisterationSchema,db:Session = Depends(get_db)):
#     return create_register_user(db,user)  

# @user_router.put("/update/{user_email}/{user_password}",response_model=UserUpdateSchema)
# def update_user(user_email:str,user_password:str,update_details:UserUpdateSchema,db:Session = Depends(get_db)):
#     return update_user_details(user_email,user_password,update_details,db) 

# @user_router.post("/login")
# def login_user(user_data:UserRequestSchemaByUserID,db:Session = Depends(get_db)):
#     return get_user_by_id(user_data,db)

# @user_router.delete("/delete/user/{email}/{password}")
# def delete_user(data : DeleteUserSchemaByUserID,db:Session = Depends(get_db)):
#     return delete_user_by_userid(data,db)

# @user_router.get("/all")
# def all_users(db:Session = Depends(get_db)):
#     return get_all_users(db)

from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime
from Eusers.schema import (
    UserRegisterationSchema,
    UserUpdateSchema,
    UserRequestSchemaByUserID,
    DeleteUserSchemaByUserID,
)
from Eusers.service import (
    create_register_user,
    update_user_details,
    get_user_by_id,
    delete_user_by_userid,
    get_all_users,
)
from database import get_db

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.post("/register")
def register_user(
    nickname: str = Form(...),
    email: str = Form(...),
    mobile_no: int = Form(...),
    full_name: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = UserRegisterationSchema(
        nickname=nickname,
        email=email,
        mobile_no=mobile_no,
        hashed_password=password,
        full_name=full_name,
        created_at=datetime.now()
    )

    result = create_register_user(db, user)
    return RedirectResponse("/login", status_code=303)


@user_router.post("/login")
def login_user(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user_data = UserRequestSchemaByUserID(email=email, password=password)
    result = get_user_by_id(user_data, db)
    return RedirectResponse("/dashboard", status_code=303)


@user_router.put("/update/{user_email}/{user_password}")
def update_user(user_email: str, user_password: str, update_details: UserUpdateSchema, db: Session = Depends(get_db)):
    return update_user_details(user_email, user_password, update_details, db)


@user_router.delete("/delete/user/{email}/{password}")
def delete_user(data: DeleteUserSchemaByUserID, db: Session = Depends(get_db)):
    return delete_user_by_userid(data, db)


@user_router.get("/all")
def all_users(db: Session = Depends(get_db)):
    return get_all_users(db)
