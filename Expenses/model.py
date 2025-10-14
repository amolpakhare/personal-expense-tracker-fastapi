from sqlalchemy import (
    Column,
    String,
    Numeric,
    Text,
    SmallInteger,
    Integer,
    BigInteger,
    Float,
    Date,
    DateTime,
    ForeignKeyConstraint,
    UniqueConstraint,
    ForeignKey,
)
from app.database import Base


class ExpenseTrackdb(Base):
    __tablename__ = "expenses_db"
    __table_args__ = (
        UniqueConstraint("emp_id","expense_id"),
        ForeignKeyConstraint(
            ["user_id"],
            [
                "app.Eusers.model.user_db",
            ],
            name="fk_user_db",
            use_alter=True,
        ),
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
    