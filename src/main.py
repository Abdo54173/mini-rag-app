from fastapi import FastAPI
from src.routes import base ,data
from src import controllers

app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)