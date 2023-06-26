from fastapi import Body
from typing import Annotated, TypedDict
from schemas.task_body import TaskBody
from schemas.category_body import CategoryBody
from models.category import CategoryEnum
from models.task import TaskEnum, Task


class TaskBodyExample(TypedDict):
    title: str
    description: str
    priority: int
    state: TaskEnum


class CategoryBodyExample(TypedDict):
    type: CategoryEnum


OptionalInt = Annotated[int | None, ...]

OptionalStr = Annotated[str | None, ...]

OptionalStateEnum = Annotated[TaskEnum | None, ...]

TaskList = list[Task]


TaskParam = Annotated[
    TaskBody,
    Body(
        example=TaskBodyExample(
            title="test", description="new text", priority=4, state=TaskEnum.PENDING
        )
    ),
]


class SearchTasksParams:
    def __init__(
        self,
        offset: OptionalInt = None,
        priority: OptionalInt = None,
        state: OptionalStateEnum = None,
    ) -> None:
        self.priority = priority
        self.state = state
        self.offset = offset


CategoryParam = Annotated[CategoryBody, ...]
