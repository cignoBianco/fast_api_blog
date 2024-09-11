from fastapi import FastAPI

app = FastAPI()


@app.get('/blog')
def index(limit, published):
    # only get 10 published blogs
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
def comments(id: int):
    # fetch comment of blog with id = id
    return {'data': {'comments': {'1', '2'}}}
