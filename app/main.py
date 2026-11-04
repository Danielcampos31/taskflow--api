
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

from app.schemas import TaskCreate, TaskRead

app = FastAPI(
    title="TaskFlow API",
    description="API inicial para gestionar tareas.",
    version="1.0.0"
)


class HealthResponse(BaseModel):
    status: str


class VersionResponse(BaseModel):
    version: str


class PingResponse(BaseModel):
    message: str


@app.get(
    "/health",
    summary="Comprobar el estado de la API",
    description="Indica si la API está funcionando correctamente.",
    response_model=HealthResponse
)
def health():
    return {"status": "ok"}


@app.get(
    "/version",
    summary="Consultar la versión",
    description="Devuelve la versión actual de TaskFlow API.",
    response_model=VersionResponse
)
def version():
    return {"version": "1.0.0"}


@app.get(
    "/ping",
    summary="Comprobar la conexión",
    description="Devuelve una respuesta para comprobar que la API responde.",
    response_model=PingResponse
)
def ping():
    return {"message": "pong"}


@app.post(
    "/tasks",
    response_model=TaskRead,
    status_code=201,
    summary="Crear una tarea temporal"
)
def create_task(task: TaskCreate):
    return TaskRead(
        id=1,
        title=task.title,
        description=task.description,
        project_id=task.project_id,
        completed=False,
        created_at=datetime.now()
    )
