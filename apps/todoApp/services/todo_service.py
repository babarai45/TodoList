import asyncio

# async def todohome():
#     await asyncio.sleep(0)
#     return {"message": "Welcome to Todo App"}



# #-----------------return html template as render----------------->

from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="apps/todoApp/templates")

def home(request: Request):
    return templates.TemplateResponse("todo.html", {"request": request})
