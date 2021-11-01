from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')#query parameter == ?limit=50&

def index(limit=10,published:bool=True,sort:Optional[str]=None):
    #only get 10 published
    if published:
        return {'data': f'{limit}blog list '}
    else:
         return {'data': f'{limit}blog from database'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id 
    return {'data': id}




@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blogs with id = id
    return {'data': {'1','2'}}

class Blog(BaseModel):
    title:str
    body:str 
    published: Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return {'data': f"Blog is creted with title as {request.title}"}
