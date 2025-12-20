from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    age: int

class Post(BaseModel):
    id: int
    title: str
    author: User


# @app.get('/')
# def home():
#     return {'data': 'message'}


# @app.get('/contacts')
# async def contacts() -> int:
#     return 34


users = [
    {'id': 1, 'name': 'Zhakhongir', 'age': 17},
    {'id': 2, 'name': 'Yusuf', 'age': 16},
    {'id': 3, 'name': 'Ulugbek', 'age': 17},
]


posts = [
    {'id': 1, 'title': 'new post 1', 'author': users[2]},
    {'id': 2, 'title': 'new post 2', 'author': users[0]},
    {'id': 3, 'title': 'new post 3', 'author': users[1]},
]


# @app.get('/news')
# async def news() -> List[Post]:
#     post_objects = []
#     for post in posts:
#         post_objects.append(Post(id=post['id'], title=post['title']))
#     return post_objects


@app.get('/news')
async def news() -> List[Post]:
    return [Post(**post) for post in posts]


@app.get('/news/{id}')
async def news_detail(id: int) -> Post:
    for post in posts:
        if post['id'] == id:
            return Post(**post)
    raise HTTPException(status_code=404, detail='Post not found')


@app.get('/search')
async def search(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return {'data': Post(**post)}
        raise HTTPException(status_code=404, detail='Post not found')
    else:
        return {'data': None}