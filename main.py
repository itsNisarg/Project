from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/blog")
def blog(limit: int = 10, published: bool = False, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}

@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created with title as {request.title}"}

@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id
    return {"data": id}

@app.get("/blog/{id}/comments")
def comments(id: int):
    # fetch comments of blog with id = id
    return {"data": {id: "comments"}}

@app.get("/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
