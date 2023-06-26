# from models.task import Task
from sqlmodel import select, Session, or_, col
from db import engine
from datetime import datetime

# from models.category import CategoryEnum
from models import CategoryEnum, Task
from fastapi import status, HTTPException, Depends, Body
from typing import Annotated
from _types import OptionalInt, SearchTasksParams, TaskList
from aiocache import cached
import uuid


BASE_URL_APP = "/api/v1/"


async def create_session() -> Session:
    with Session(engine) as session:
        return session


async def get_tasks(offset: OptionalInt = 0) -> TaskList:
    with Session(bind=engine) as session:
        return session.exec(select(Task).offset(offset).limit(10)).all()


@cached(ttl=3600)  # especifica el tiempo de vida del caché en segundos (opcional)
async def get_cached_tasks(offset: OptionalInt = 0) -> TaskList:
    response = await get_tasks(offset=offset)
    return response


GetTasksDep = Annotated[TaskList | list, Depends(get_cached_tasks)]


async def create_task() -> Task:
    task = Task(**task_body.dict())
    task.created_at = date

    return task


CreateSessionDep = Annotated[Session, Depends(create_session)]

SearchTasksParamsDep = Annotated[SearchTasksParams, Depends(SearchTasksParams)]


async def search_task_by_id(id: OptionalInt) -> Task:
    with Session(engine) as session:
        if result := session.exec(select(Task).where(id == Task.id)).first():
            return result

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


SearchTaskDep = Annotated[Task, Depends(search_task_by_id)]


async def search_tasks_by_filter(
    search_params: SearchTasksParamsDep,
) -> TaskList:
    with Session(engine) as session:
        if result := session.exec(
            select(Task)
            .where(
                or_(
                    col(Task.priority) == search_params.priority,
                    col(Task.state) == search_params.state,
                )
            )
            .offset(search_params.offset)
            .limit(10)
        ).fetchall():
            return result

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


TaskListDep = Annotated[TaskList, Depends(search_tasks_by_filter)]


async def current_date() -> datetime:
    format = "%Y-%m-%d %H:%M:%S"
    date = datetime.now().strftime(format)

    return datetime.strptime(date, format)


CurrentDateDep = Annotated[datetime, Depends(current_date)]


async def delete_task() -> None:
    ...


async def generate_uuid() -> uuid.UUID:
    return uuid.uuid4()
