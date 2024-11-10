""" Home API

This module contains the API for the home page. It is responsible for rendering the home page.


 """


#  *******************************************************************
#         ************ simple api of function ************* 
# *******************************************************************

#_______01
# from fastapi import APIRouter
# from apps.homeApp.services.home_service import get_home_message

# router = APIRouter()

# @router.get("/")
# def home():
#     return {"message": get_home_message()}



# #*******************************************************************
#         ************ async api of function *************
# #*******************************************************************


#_______02
# import asyncio
# from fastapi import APIRouter
# from apps.homeApp.services.home_service import get_home_message

# router = APIRouter()

# @router.get("/")
# async def home():
#     message = await get_home_message()
#     return {"message": message}




#_______03
# #*******************************************************************
#         ************ async api of class *************
# #*******************************************************************

# import asyncio
# from fastapi import APIRouter
# from apps.homeApp.services.home_service import HomeService

# router = APIRouter()
# home_service = HomeService()  # create an instance of HomeService

# @router.get("/")
# async def home():
#     message = await home_service.get_home_message()
#     return {"message": message}








# #*******************************************************************
#         ************ template rendering *************
# #*******************************************************************

#__01
# #-----------------simple template rendering by function--------------


# from fastapi import APIRouter, Request
# from apps.homeApp.services.home_service import home as get_home_template

# router = APIRouter()

# @router.get("/")
# def home(request: Request):
#     response = get_home_template(request)
#     return response




# #*******************************************************************
#         ************ async template rendering *************
# #*******************************************************************

#__02
# #-----------------asyn template rendering by function--------------


# from fastapi import APIRouter, Request
# from apps.homeApp.services.home_service import home as get_home_template

# router = APIRouter()

# @router.get("/")
# async def home(request: Request):
#         response = await get_home_template(request)
#         return response






# #*******************************************************************
#         ************ class based api for template rendering *************
# #*******************************************************************


# #_______03
# #-----------------class based api for template rendering--------------



#-----------crud api----------------

# apps/homeApp/apis/home_api.py
from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.ext.asyncio import AsyncSession
from database.db_conn import async_session
from apps.homeApp.schemas.home_schema import StudentCreate, StudentUpdate
from apps.homeApp.services.home_service import get_students, create_student, get_student, update_student, delete_student
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from database.db_conn import get_db
from starlette.status import HTTP_302_FOUND

router = APIRouter(
    tags=["HomeAPI"]
)
templates = Jinja2Templates(directory="apps/homeApp/templates")

async def get_db():
    async with async_session() as session:
        yield session

@router.get("/students")
async def list_students(request: Request, db: AsyncSession = Depends(get_db)):
    students = await get_students(db)
    return templates.TemplateResponse("students/list.html", {"request": request, "students": students})

@router.get("/students/create")
async def create_student_form(request: Request):
    return templates.TemplateResponse("students/create.html", {"request": request})

@router.post("/students/create")
async def add_student(
    name: str = Form(...), email: str = Form(...), address: str = Form(""), phone: str = Form(""),
    student_class: str = Form(...), subject: str = Form(""), db: AsyncSession = Depends(get_db)
):
    student_data = StudentCreate(name=name, email=email, address=address, phone=phone, student_class=student_class, subject=subject)
    await create_student(db, student_data)
    return RedirectResponse(url="/students", status_code=HTTP_302_FOUND)


@router.post("/students/create")
async def create_student_endpoint(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    return await create_student(db=db, student=student)

@router.get("/students/update/{student_id}")
async def update_student_form(request: Request, student_id: int, db: AsyncSession = Depends(get_db)):
    student = await get_student(db, student_id)
    return templates.TemplateResponse("students/update.html", {"request": request, "student": student})

@router.post("/students/update/{student_id}")
async def update_student_data(
    student_id: int, name: str = Form(...), email: str = Form(...), address: str = Form(""),
    phone: str = Form(""), student_class: str = Form(...), subject: str = Form(""), db: AsyncSession = Depends(get_db)
):
    student_data = StudentUpdate(name=name, email=email, address=address, phone=phone, student_class=student_class, subject=subject)
    await update_student(db, student_id, student_data)
    return RedirectResponse(url="/students", status_code=HTTP_302_FOUND)

@router.get("/students/delete/{student_id}")
async def delete_student_data(student_id: int, db: AsyncSession = Depends(get_db)):
    await delete_student(db, student_id)
    return RedirectResponse(url="/students", status_code=HTTP_302_FOUND)













