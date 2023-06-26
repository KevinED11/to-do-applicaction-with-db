from sqlmodel import Field, SQLModel
from enum import StrEnum
from datetime import datetime


class TaskEnum(StrEnum):
    IN_PROGRESS = "open"
    PENDING = "pending"
    COMPLETED = "complete"


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(
        default=..., index=True, nullable=False, min_length=4, max_length=40
    )
    description: str | None = Field(default=None, min_length=15, max_length=100)
    created_at: datetime | None = Field(default=None)
    priority: int = Field(ge=2, le=10, index=True, nullable=False)
    state: TaskEnum = Field(default=TaskEnum.PENDING, nullable=False, index=True)
    category_id: int | None = Field(default=None, foreign_key="category.id")


# user_id: int | None = Field(default=None, foreign_key="user.id")
