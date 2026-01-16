from fastapi import FastAPI

app = FastAPI()

#Hello world API
@app.get("/hello")
def root():
    return {"msg": "Hello"}
