from fastapi import APIRouter, status, Response, Path
from sqlmodel import Session
from models.task import Task, TaskEnum
from models.category import Category
from db import engine
from typing import Annotated
from dependencies import (
    CreateSessionDep,
    SearchTaskDep,
    TaskListDep,
    CurrentDateDep,
    GetTasksDep,
    BASE_URL_APP,
)
from _types import (
    TaskParam,
    TaskList,
)
from documentation.body_examples import task_body_example, category_body_example
from schemas.category_body import CategoryBody
from tags import Tags


tasks = APIRouter(prefix=BASE_URL_APP + "tasks", tags=[Tags.TASKS])


@tasks.get("/", response_model=TaskList)
async def read_tasks(
    tasks: GetTasksDep,
):
    return tasks


@tasks.post("/create/", response_class=Response)
async def create(
    task_body: TaskParam,
    category_body: CategoryBody,
    date: CurrentDateDep,
):
    task = Task(**task_body.dict())
    task.created_at = date

    # category = Category(**category_body.dict())

    with Session(engine) as session:
        session.add(task)
        # session.add(category)
        session.commit()

    return Response(
        content="he task has been successfully created",
        status_code=status.HTTP_201_CREATED,
    )


@tasks.get("/{id}", response_model=Task)
async def filter_task_by_id(
    id: Annotated[int, Path(description="The id of the task")],
    task: SearchTaskDep,
):
    return task


@tasks.get("/filter/", response_model=TaskList)
async def filter_tasks(tasks: TaskListDep):
    return tasks


@tasks.patch("/update/{id}", response_model=Task)
async def update(
    id: Annotated[int, Path(ge=1, title="The id of the user to update")],
    new_task_info: TaskParam,
    existing_task: SearchTaskDep,
    session: CreateSessionDep,
):
    for key, value in new_task_info.dict(exclude_unset=True).items():
        setattr(existing_task, key, value)

    session.add(existing_task)
    session.commit()
    session.refresh(existing_task)
    session.close()

    return existing_task


@tasks.delete("/delete/{id}", response_class=Response)
async def delete(id: int, task: SearchTaskDep, session: CreateSessionDep):
    session.delete(task)
    session.commit()
    session.close()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
