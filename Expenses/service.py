from Expenses.model import ExpenseTrackDB
from database import Base
from Expenses.schema import (ExpenseCreateSchema, ExpenseUpdateSchema,ExpenseRequestSchemaByExpenseID,DeleteExpenseSchemaByExpenseID)
from fastapi import HTTPException, status

#post api for expenses

def create_expense(db,expense:ExpenseCreateSchema):
    new_expense = ExpenseTrackDB(
        title=expense.title,
        amount=expense.amount,
        date=expense.date,
        category=expense.category,
        description=expense.description,
        user_id=expense.user_id,
        created_at=expense.created_at
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

#put api for update expenses
def update_expense(update_details:ExpenseUpdateSchema,db):
    expense = db.query(ExpenseTrackDB).filter(ExpenseTrackDB.expense_id==update_details.expense_id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Expense not found")
    expense.title = update_details.title
    expense.amount = update_details.amount
    expense.date = update_details.date
    expense.category = update_details.category
    expense.description = update_details.description
    expense.user_id = update_details.user_id
    expense.updated_at = update_details.updated_at
    db.commit()
    db.refresh(expense)
    return expense

# get api for get expense by expense id
def get_expense_by_id(expense:ExpenseRequestSchemaByExpenseID,db):
    expense = db.query(ExpenseTrackDB).filter(ExpenseTrackDB.expense_id == expense.expense_id 
                                              and ExpenseTrackDB.user_id == expense.user_id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Expense not found")
    return expense

#put api for delete expense by expense id
def delete_expense_by_expenseid(data:DeleteExpenseSchemaByExpenseID,db):
    expense = db.query(ExpenseTrackDB).filter(ExpenseTrackDB.expense_id==data.expense_id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Expense not found")
    expense.deleted_at = data.deleted_at
    db.commit()
    db.refresh(expense)
    db.delete(expense)
    db.commit()
    return "Expense deleted successfully"

# get api for get all expenses
def get_all_expenses(db):
    expenses = db.query(ExpenseTrackDB).all()
    return expenses

