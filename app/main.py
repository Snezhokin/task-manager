from fastapi import FastAPI

app=FastAPI(title="Task Manager with FastApi")

@app.get("/")
def root():
    return {"message":"Welcome to Task Manager with FastApi"}