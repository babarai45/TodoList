# # main.py
from fastapi import FastAPI
from routers.main_router import all_router

app = FastAPI(
    title="FastAPI with React",
    description="FastAPI with React",

)

app.include_router(all_router)  # 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)






#-------------------------------------------------------------------
# for homeapp with react
# # main.py
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from apps.homeApp.apis.home_api import router as home_router
# from database.db_conn import init_db

# app = FastAPI()

# # Allowing CORS for React frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Update this with your frontend's URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(home_router)

# @app.on_event("startup")
# async def on_startup():
#     await init_db()

