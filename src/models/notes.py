from pydantic import BaseModel
from datetime import datetime

class Notes(BaseModel):
    id: int
    title: str
    content: str
    timestamp: datetime
