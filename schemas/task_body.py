from pydantic import BaseModel, Field
from models.task import TaskEnum


class TaskBody(BaseModel):
    title: str = Field(..., min_length=4, max_length=40)
    description: str | None = Field(default=None, min_length=15, max_length=100)
    priority: int = Field(ge=2, le=10, nullable=False)
    state: TaskEnum = Field(default=TaskEnum.PENDING, nullable=False)
