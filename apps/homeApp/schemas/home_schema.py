# apps/homeApp/schemas/home_schema.py
from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: str
    address: Optional[str] = None
    phone: Optional[str] = None
    student_class: str
    subject: Optional[str] = None

class StudentCreate(BaseModel):
    std_name: str
    std_email: str
    std_address: str
    std_phone: str
    std_class: str
    std_subject: str
    
class StudentUpdate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int

    class Config:
        orm_mode = True
