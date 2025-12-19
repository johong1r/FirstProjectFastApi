from fastapi import FastAPI, HTTPException
from typing import Optional


app = FastAPI()


@app.get('/')
def home():
    return {'data': 'message'}


@app.get('/contacts')
async def contacts() -> int:
    return 34


posts = [
    {'id': 1, 'title': 'new post 1',},
    {'id': 2, 'title': 'new post 2',},
    {'id': 3, 'title': 'new post 3',},
]


@app.get('/news/{id}')
async def news(id: int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=404, detail='Post not found')


@app.get('/search')
async def search(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return post
        raise HTTPException(status_code=404, detail='Post not found')
    else:
        return {'data': 'No post id provided'}