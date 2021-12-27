from datetime import datetime
from pydantic import BaseModel


class Creator(BaseModel):
    e_id: int
    metadata: str
    datetime: datetime


class Consumer(BaseModel):
    e_id: int
    metadata: str
    description: str
    cmdb_id: int


class LoggerEvent(BaseModel):
    type: str
    message: str
    event: str
    creator: Creator
    consumer: Consumer
