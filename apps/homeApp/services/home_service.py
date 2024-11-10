# apps/homeApp/services/home_service.py
""" This file contains the service functions for the home app. 
    The service functions are responsible for handling the business logic of the home app.

"""
#_________01
#************simple service of simple function*************

# def get_home_message():
#     return "I am home page by simple function"



#_________02
#************simple service of async function*************

# async def get_home_message():
#     await asyncio.sleep(0)
#     return "i am home page by async function"


#_________03
#************simple service of class async function*************
# import asyncio
# class HomeService:
#     async def get_home_message(self):
#         await asyncio.sleep(0)
#         return "i am home page by class based async function"






#****______________________________________________________________************
#****|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||************





#*******************************************************************
        #************ template rendering*************
#*******************************************************************

#_________01
#-----------------simple template rendering by function---------------------
# from fastapi import Request
# from fastapi.templating import Jinja2Templates

# templates = Jinja2Templates(directory="apps/homeApp/templates")

# def home(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request})



#*******************************************************************
#************ async template rendering*************
#*******************************************************************


#_________02
#-----------------async template rendering by function---------------------

# from fastapi import Request
# from fastapi.templating import Jinja2Templates
# import asyncio

# templates = Jinja2Templates(directory="apps/homeApp/templates")

# async def home(request: Request):
#     await asyncio.sleep(0)
#     return templates.TemplateResponse("home.html", {"request": request})







#***********************************************************************************
#*****************class based servive for template rendering**********
#***********************************************************************************



# _________03
# -----------------class based service for template rendering---------------------
# from fastapi import Request
# from fastapi.templating import Jinja2Templates
# import asyncio

# templates = Jinja2Templates(directory="apps/homeApp/templates")

# class HomeService:
#     async def home_template(self, request: Request):
#         await asyncio.sleep(0)
#         return templates.TemplateResponse("home.html", {"request": request})
    


#-----------------------crud operation---------------------

# apps/homeApp/services/home_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from apps.homeApp.models.home_model import Student
from apps.homeApp.schemas.home_schema import StudentCreate, StudentUpdate



async def get_students(db: AsyncSession):
    result = await db.execute(select(Student))
    return result.scalars().all()

async def create_student(db: AsyncSession, student_data: StudentCreate):
    student = Student.from_orm(student_data)
    db.add(student)
    await db.commit()
    await db.refresh(student)
    return student

async def get_student(db: AsyncSession, student_id: int):
    return await db.get(Student, student_id)

async def update_student(db: AsyncSession, student_id: int, student_data: StudentUpdate):
    student = await get_student(db, student_id)
    if student:
        for key, value in student_data.dict(exclude_unset=True).items():
            setattr(student, key, value)
        await db.commit()
        await db.refresh(student)
    return student

async def delete_student(db: AsyncSession, student_id: int):
    student = await get_student(db, student_id)
    if student:
        await db.delete(student)
        await db.commit()
    return student







