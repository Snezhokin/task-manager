from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.tasks import router as tasks_router

app = FastAPI(title="Task Manager with FastApi")

app.include_router(user_router)
app.include_router(tasks_router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Manager with FastApi"}