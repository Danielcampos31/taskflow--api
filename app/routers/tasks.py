
from datetime import datetime
from fastapi import APIRouter

from app.schemas import TaskCreate, TaskRead

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.post(
    "",
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
