from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id
    return {"data": id}
