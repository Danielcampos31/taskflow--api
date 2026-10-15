
from fastapi import FastAPI
from pydantic import BaseModel

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
