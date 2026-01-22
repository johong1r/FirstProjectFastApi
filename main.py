from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from typing import Optional, List, Dict, Annotated
from sqlalchemy.orm import Session
from models import Base, User, Post
from database import engine, session_local
from schemas import UserCreate, User as dbUser, PostCreate, PostResponse


app = FastAPI()


Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post('/users/', response_model=dbUser)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user




# @app.get('/news')
# async def news() -> List[Post]:
#     post_objects = []
#     for post in posts:
#         post_objects.append(Post(id=post['id'], title=post['title']))
#     return post_objects


# @app.get('/news')
# async def news() -> List[Post]:
#     return [Post(**post) for post in posts]


# @app.get('/news/{id}')
# async def news_detail(id: Annotated[int, Path(..., title='Тут ID', ge=1, lt=1000)]) -> Post:
#     for post in posts:
#         if post['id'] == id:
#             return Post(**post)
#     raise HTTPException(status_code=404, detail='Post not found')


# @app.get('/search')
# async def search(post_id: Annotated[Optional[int], Query(title='ID из поста для поиска', ge=1, le=50)]) -> Dict[str, Optional[Post]]:
#     if post_id:
#         for post in posts:
#             if post['id'] == post_id:
#                 return {'data': Post(**post)}
#         raise HTTPException(status_code=404, detail='Post not found')
#     else:
#         return {'data': None}
    

# @app.post('/news/create')
# async def create_news(post: PostCreate) -> Post:
#     author = next((user for user in users if user['id'] == post.author_id), None)

#     if not author:
#         raise HTTPException(detail='User not found', status_code=404)
    
#     new_post_id = len(posts) + 1

#     new_post = {'id': new_post_id, 'title': post.title, 'author': author}
#     posts.append(new_post)

#     return Post(**new_post)


# @app.post('/users/create')
# async def create_users(user: Annotated[
#     UserCreate,
#     Body(..., example={
#         'name': 'UserName',
#         'age': 1
#     })
# ]) -> Post:
    
    
#     new_user_id = len(users) + 1

#     new_user = {'id': new_user_id, 'name': user.name, 'age': user.age}
#     posts.append(new_user)

#     return Post(**new_user)


# # @app.put('/news/update/{id}')
# # async def update_news(post: PostUpdate) -> Post:
# #     author = next((user for user in users if user['id'] == post.author_id), None)

# #     if not author:
# #         raise HTTPException(detail='User not found', status_code=404)
    
# #     update_post_id = len(posts) + 1

# #     update_post = {'id': update_post_id, 'title': post.title, 'author': author}
# #     posts.append(update_post)

# #     return Post(**update_post)