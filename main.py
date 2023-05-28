from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/blog")
def blog(limit: int = 10, published: bool = False):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}

@app.post("/blog")
def create_blog():
    return {"data": "Blog is created"}

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
