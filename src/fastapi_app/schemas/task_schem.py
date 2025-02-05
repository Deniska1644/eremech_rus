from pydantic import BaseModel
from datetime import date
from typing import Optional, List


class GetTask(BaseModel):
    id: int
    title: str
    description: str
    due_data: date

    class Config:
        orm_mode = True
        from_attributes = True


class ListTask(BaseModel):
    task_list: List[GetTask]


class CreateTask(BaseModel):
    title: str
    description: str
    due_data: date
