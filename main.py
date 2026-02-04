from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "FastAPI running"}

@app.get("/about")
def about():
    return {"messege":'my name i swalih'}


 



