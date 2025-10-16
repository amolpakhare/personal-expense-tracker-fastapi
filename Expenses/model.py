
from sqlalchemy import (
    Column,
    String,
    Text,
    SmallInteger,
    Integer,
    Float,
    Date,
    DateTime,
    ForeignKeyConstraint,
    UniqueConstraint
)
from sqlalchemy.orm import relationship
from database import Base


class ExpenseTrackDB(Base):
    __tablename__ = "expenses_db"
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_id"],
            ["user_db.user_id"],  
            name="fk_user_db",
            use_alter=True,
            ondelete="CASCADE"
        ),
        {'schema': None} 
    )
    expense_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    user = relationship("UserDB", back_populates="expenses")
