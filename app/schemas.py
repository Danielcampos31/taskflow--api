
from datetime import datetime
from pydantic import BaseModel, Field


# Modelo para crear una tarea
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None
    project_id: int


# Modelo para consultar una tarea
class TaskRead(TaskCreate):
    id: int
    completed: bool
    created_at: datetime


# Modelo para crear un proyecto
class ProjectCreate(BaseModel):
    name: str
    description: str


# Modelo para consultar un proyecto
class ProjectRead(ProjectCreate):
    id: int
    created_at: datetime
