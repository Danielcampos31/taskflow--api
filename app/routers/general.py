
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    tags=["general"]
)


class HealthResponse(BaseModel):
    status: str


class VersionResponse(BaseModel):
    version: str


class PingResponse(BaseModel):
    message: str


@router.get(
    "/health",
    summary="Comprobar el estado de la API",
    description="Indica si la API está funcionando correctamente.",
    response_model=HealthResponse
)
def health():
    return {"status": "ok"}


@router.get(
    "/version",
    summary="Consultar la versión",
    description="Devuelve la versión actual de TaskFlow API.",
    response_model=VersionResponse
)
def version():
    return {"version": "1.0.0"}


@router.get(
    "/ping",
    summary="Comprobar la conexión",
    description="Devuelve una respuesta para comprobar que la API responde.",
    response_model=PingResponse
)
def ping():
    return {"message": "pong"}


# Ruta temporal para comprobar el manejo global de excepciones.
@router.get("/error")
def provocar_error():
    raise RuntimeError("Este es un error de prueba")
