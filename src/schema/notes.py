from pydantic import BaseModel
from datetime import datetime


class NoteCreate(BaseModel):
    title: str
    content: str
    datetime: datetime

class NoteResponse(NoteCreate):
    id: int

    class Config:
        orm_mode = True
