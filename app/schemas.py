from pydantic import BaseModel
from fastapi_users import schemas
import uuid


class PostCreate(BaseModel):
    Title : str
    Content : str

class PostResponse(BaseModel):
    Title : str
    Content : str

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass