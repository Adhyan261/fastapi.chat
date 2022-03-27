from pickle import NONE
from turtle import title
from fastapi import FastAPI
from random import randrange
from . import models
from .database import engine
from .routers import user,post,auth,vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message":"Hello"}



