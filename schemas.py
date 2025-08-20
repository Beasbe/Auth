from pydantic import BaseModel

class CredsSchema(BaseModel):
    login: str
    password: str

class CredsGetSchema(BaseModel):
    id: int
    login: str
    password: str
