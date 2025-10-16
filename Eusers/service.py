from Eusers.model import UserDB as user_db
from database import Base
from Eusers.schema import (UserRegisterationSchema, UserUpdateSchema,UserLoginSchema,DeleteUserSchemaByUserID,UserRequestSchemaByUserID)
from fastapi import HTTPException, status
from Eusers.transformer import *


#post api User Regestration
def create_register_user(db,user:UserRegisterationSchema):
    already_user = db.query(user_db).filter(user_db.email==user.email).first()
    if already_user:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User already exists")
    new_user = user_db(
        nickname=user.nickname,
        email=user.email,
        mobile_no=user.mobile_no,
        hashed_password=user.hashed_password,
        full_name=user.full_name,
        is_active=user.is_active,
        created_at=user.created_at
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# put api Update user details
def update_user_details(user_email:str,user_password:str,update_details:UserUpdateSchema,db):
    user = db.query(user_db).filter(user_db.email==user_email,
                                    user_db.hashed_password==user_password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    user.nickname = update_details.nickname
    user.email = update_details.email
    user.mobile_no = update_details.mobile_no
    user.hashed_password = update_details.hashed_password
    user.full_name = update_details.full_name
    user.is_active = update_details.is_active
    user.updated_at = update_details.updated_at
    db.commit()
    db.refresh(user)
    return user

# get api Get user details by user id
def get_user_by_id(user_data: UserRequestSchemaByUserID, db):
    users = db.query(user_db).filter(
        user_db.email == user_data.email,
        user_db.hashed_password == user_data.password
    ).all()

    total = len(users)
    if total == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return get_euser_data_transformer((users, total))
    


#put api Delete user details by user id
def delete_user_by_userid(data:DeleteUserSchemaByUserID,db):
    user = db.query(user_db).filter(user_db.user_id==data.User_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    user.deleted_at = data.deleted_at
    db.commit()
    db.refresh(user)
    return user



#get api get all of list of users
def get_all_users(db):
    users = db.query(user_db).all()
    return users
