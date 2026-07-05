from pydantic import BaseModel, ConfigDict
class CreatePost(BaseModel):
    content : str

class PostResponse(BaseModel):
    id: int
    content: str

    model_config = ConfigDict(from_attributes=True)