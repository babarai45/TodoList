# from fastapi import APIRouter
# from apps.todoApp.services.todo_service import home as todohome


# router = APIRouter(
#     prefix="/TodoApp"
# )


# ----------------returm simple wellcome message  api -------------------->
# @router.get('/todo')
# async def get_todo_home():
#     message = await todohome()
#     return {"message": message}




#--------------------retuern templete as render




from fastapi import APIRouter, Request
from apps.todoApp.services.todo_service import home as get_home_template

router = APIRouter(
    prefix="/home",

    tags= ["TodoApi"]
)

@router.get("/todo")
def home(request: Request):
    response = get_home_template(request)
    return response