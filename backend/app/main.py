from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, schemas, crud, database

app = FastAPI()

@app.on_event("startup")
def on_start():
    models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos/", response_model=list[schemas.TodoOut])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)