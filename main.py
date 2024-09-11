from fastapi import FastAPI

from typing import Optional

app = FastAPI()


@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs list from the db'}
    else:
        return {'data': f'{limit} unpublished blogs list from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit = 10):
    # fetch comment of blog with id = id
    return {'data': f'{limit} comments'}
