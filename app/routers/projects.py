
from fastapi import APIRouter

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)


@router.get(
    "",
    summary="Consultar los proyectos"
)
def get_projects():
    return []
