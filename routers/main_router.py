# routers/main_router.py
from fastapi import APIRouter
from apps.homeApp.apis.home_api import router as home_router
from apps.todoApp.apis.todo_api import router as todo_router

all_router = APIRouter(
    prefix="/api",
)


all_router.include_router(home_router,)

all_router.include_router(todo_router)



