from sqlalchemy import Boolean, String, Column, Integer, DateTime, func
from datetime import datetime
from core.database import Base


class UserModel(Base):
    __tablename__ = "Users"

    id: Column(Integer, primary_key=True, index=True)
    email: Column(String(255), nullable=False, unique=True, index=True)
    password: Column(String(100), nullable=False)
    created_at: Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    updated_at: Column(DateTime, nullable=False, server_default=func.now())