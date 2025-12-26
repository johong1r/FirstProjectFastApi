from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict
from pydantic import BaseModel


app = FastAPI()


class PostCreate(BaseModel):
    title: str
    author_id: int


class PostUpdate(BaseModel):
    title: str
    author_id: int


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
    

@app.post('/news/create')
async def create_news(post: PostCreate) -> Post:
    author = next((user for user in users if user['id'] == post.author_id), None)

    if not author:
        raise HTTPException(detail='User not found', status_code=404)
    
    new_post_id = len(posts) + 1

    new_post = {'id': new_post_id, 'title': post.title, 'author': author}
    posts.append(new_post)

    return Post(**new_post)


# @app.put('/news/update/{id}')
# async def update_news(post: PostUpdate) -> Post:
#     author = next((user for user in users if user['id'] == post.author_id), None)

#     if not author:
#         raise HTTPException(detail='User not found', status_code=404)
    
#     update_post_id = len(posts) + 1

#     update_post = {'id': update_post_id, 'title': post.title, 'author': author}
#     posts.append(update_post)

#     return Post(**update_post)