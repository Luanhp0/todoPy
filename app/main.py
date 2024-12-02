from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base
from .dependencies import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/tasks/")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), user_id: int = 1):
    return crud.create_task(db=db, task=task, user_id=user_id)

@app.get("/tasks/")
def read_tasks(db: Session = Depends(get_db), user_id: int = 1):
    return crud.get_tasks(db=db, user_id=user_id)
