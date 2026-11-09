
import time
import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routers import general, tasks, projects

# Configuración del registro de errores.
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="TaskFlow API",
    description="API inicial para gestionar tareas.",
    version="1.0.0"
)

# CORS: permite las peticiones del frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Process-Time"]
)


# Manejador global de excepciones.
@app.exception_handler(Exception)
async def manejar_excepcion_global(request: Request, exc: Exception):
    # Guarda el error completo en los registros internos.
    logger.exception("Error interno en la API")

    # Devuelve un mensaje genérico sin mostrar el stacktrace.
    return JSONResponse(
        status_code=500,
        content={"error": "Error interno del servidor"}
    )


# Middleware personalizado para medir el tiempo de respuesta.
@app.middleware("http")
async def medir_tiempo_peticion(request: Request, call_next):
    inicio = time.perf_counter()

    try:
        response = await call_next(request)
    except Exception as exc:
        # Utiliza el manejador global también para estas excepciones.
        response = await manejar_excepcion_global(request, exc)

    tiempo_ms = (time.perf_counter() - inicio) * 1000

    response.headers["X-Process-Time"] = f"{tiempo_ms:.2f}"

    return response


# Registro de los routers.
app.include_router(general.router)
app.include_router(tasks.router)
app.include_router(projects.router)
