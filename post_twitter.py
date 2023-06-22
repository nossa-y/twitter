from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Annotated
import json


class Post(BaseModel):
    title : str
    description : str = None
    url : str = None
    comment : str = None

class UpdatePost(BaseModel):
    title : str = None
    description : str =None
    url : str = None                 #à revoir
    comment : str = None
    likes : 

posts = {
    1: {
        "title" : "first post",
        "description" : "pretty easy",
        "comment" : "dropping the first comment"
        "likes" : 2
    }
}

app = FastAPI()

@app.get("/post/")
def get_all_post():
    all=[]
    for post in posts:
        all.append(post)
    return all

@app.get("/post/{id}")
def get_one_post(id):
    return posts[id]

@app.post("/")
def to_post(post: Post):
    posts.update({len(json.loads(posts)):post})
    return posts

@app.put("/post/{id}", response_model = Post )
def update_post(id, new_post:UpdatePost):
    if UpdatePost.title is not None:
        posts[id].title = UpdatePost.title
    if UpdatePost.description is not None:
        posts[id].description = UpdatePost.description
    if UpdatePost.url is not None:
        posts[id].url = UpdatePost.url
    if UpdatePost.comment is not None:
        posts[id].comment = UpdatePost.comment
    return posts[id]

@app.put("/post/{id}")
def like_post(id):

@app.put("/post/{id}")
def comment_post(id):


@app.delete("/post/{id}")
def remove_post(id):
    if posts[id] is not None:
        del posts[id]


    

    
