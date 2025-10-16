from sqlalchemy import (
    Column,
    String,
    Integer,
    SmallInteger,
    DateTime,
    UniqueConstraint
)
from sqlalchemy.orm import relationship
from database import Base

class UserDB(Base):
    __tablename__ = "user_db"
    __table_args__ = (UniqueConstraint("email", name="uq_user_email"),)

    user_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nickname = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    mobile_no = Column(Integer, unique=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    is_active = Column(SmallInteger, default=1)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    expenses = relationship("ExpenseTrackDB", back_populates="user")
