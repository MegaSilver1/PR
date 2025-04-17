
from pydantic import BaseModel

class TaskBase(BaseModel):  # для fastapi
    title: str
    completed: bool = False # таск не завершен


class TaskCreate(TaskBase): # для fastapi
    pass

class TaskUpdate(TaskBase): # для fastapi
    pass

class Task(TaskBase): # модель тасков
    id: int

    class Config:
        orm_mode = True
