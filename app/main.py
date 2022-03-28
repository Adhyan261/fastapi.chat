from pickle import NONE
from turtle import title
import fastapi
fastapi.use('Agg')
from fastapi import FastAPI
FastAPI.use('Agg')
from random import randrange
from . import models
from .database import engine
from .routers import user,post,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
CORSMiddleware.use('Agg')


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hellooo"}




