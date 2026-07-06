from pydantic import BaseModel, ConfigDict
class CreatePost(BaseModel):                        ##request model
    content : str

class PostResponse(BaseModel):                      ##response model
    id: int
    content: str

    model_config = ConfigDict(from_attributes=True)

class CreateUser(BaseModel):                        ##request model
    email: str
    password: str

class UserResponse(BaseModel):                      ##response model
    id: int
    email: str

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: str
    password: str