from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    age: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class PostBase(BaseModel):
    title: str
    author_id: int  


class PostCreate(PostBase):
    pass


class PostResponse(BaseModel):
    id: int
    title: str
    author: User

    model_config = ConfigDict(from_attributes=True)
