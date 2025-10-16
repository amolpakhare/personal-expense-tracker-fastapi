from pydantic import BaseModel, EmailStr
from typing import Optional  
from datetime import datetime

class ExpenseBaseSchema(BaseModel):
    title: Optional[str]=None
    amount: Optional[float]=None
    date: Optional[datetime]=None
    category: Optional[str]=None
    description: Optional[str]=None
    user_id: Optional[int]=None

class ExpenseCreateSchema(ExpenseBaseSchema):
    created_at: Optional[datetime]=None

class ExpenseUpdateSchema(ExpenseBaseSchema):
    expense_id:int
    updated_at: datetime

class ExpenseResponseSchema(ExpenseBaseSchema):
    expense_id:int
    updated_at: Optional[datetime]=None
    deleted_at: Optional[datetime]=None
    class Config:
        orm_mode = True

class ExpenseRequestSchemaByExpenseID(BaseModel):
    expense_id:Optional[int]=None
    user_id:Optional[int]=None

class DeleteExpenseSchemaByExpenseID(BaseModel):
    expense_id:Optional[int]=None
    user_id:Optional[int]=None
    deleted_at: Optional[datetime]=None