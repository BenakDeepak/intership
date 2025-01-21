from fastapi import FastAPI
from app.routes import user
from app.database.database import Base, engine

app = FastAPI()


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}