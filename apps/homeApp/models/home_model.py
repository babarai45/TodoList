# apps/homeApp/models/home_model.py
from sqlmodel import SQLModel, Field
from typing import Optional

class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    address: Optional[str] = None
    phone: Optional[str] = None
    student_class: str
    subject: Optional[str] = None
