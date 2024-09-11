from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'blog list'}


@app.get('/blog/{id}')
def show(id):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comment of blog with id = id
    return {'data': {'comments': {'1', '2'}}}
