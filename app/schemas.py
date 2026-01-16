from pydantic import BaseModel

class PostCreate(BaseModel):
    Title : str
    Content : str

class PostResponse(BaseModel):
    Title : str
    Content : str
