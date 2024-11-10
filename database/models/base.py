# database/models/base.py
from sqlmodel import SQLModel

# Base for SQLModel classes (automatically available in SQLModel)
class Base(SQLModel):
    pass
