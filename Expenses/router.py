from fastapi import APIRouter, Depends
from Expenses.schema import (ExpenseCreateSchema, ExpenseUpdateSchema, ExpenseRequestSchemaByExpenseID, DeleteExpenseSchemaByExpenseID, ExpenseResponseSchema)
from Expenses.service import (create_expense, update_expense, get_expense_by_id, delete_expense_by_expenseid, get_all_expenses)
from database import get_db
from sqlalchemy.orm import Session  

expense_router = APIRouter(
    prefix="/expenses",
    tags=["expenses"]
)

@expense_router.post("/create")
def create_new_expense(expense: ExpenseCreateSchema, db: Session = Depends(get_db)):
    return create_expense(db, expense)  

@expense_router.put("/update/expense")
def update_existing_expense(update_details: ExpenseUpdateSchema, db: Session = Depends(get_db)):
    return update_expense(update_details, db)

@expense_router.post("/get/expense")
def get_expense(expense: ExpenseRequestSchemaByExpenseID, db: Session = Depends(get_db)):
    return get_expense_by_id(expense, db)

@expense_router.delete("/delete/expense")
def delete_expense(data: DeleteExpenseSchemaByExpenseID, db: Session = Depends(get_db)):
    return delete_expense_by_expenseid(data, db)

@expense_router.get("/all")
def all_expenses(db: Session = Depends(get_db)):
    return get_all_expenses(db)