
from fastapi import FastAPI

from app.routers import general, tasks, projects

app = FastAPI(
    title="TaskFlow API",
    description="API inicial para gestionar tareas.",
    version="1.0.0"
)

app.include_router(general.router)
app.include_router(tasks.router)
app.include_router(projects.router)
