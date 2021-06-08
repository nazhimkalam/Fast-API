# Importing Libraries
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# Creating the API Endpoints
@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/welcome")
def getName(name: str, age: int):
    return {"messsage": "Welcome " + name + " and you are " + str(age) + " years old"}


# By deafult endpoint url  http://127.0.0.1:8000
