from sqlmodel import Field, SQLModel
from enum import StrEnum


class CategoryEnum(StrEnum):
    PERSONAL = "personal"
    WORK = "work"
    SHOPPING = "shopping"
    OTHER = "other"


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: CategoryEnum = Field(default=CategoryEnum.WORK, index=True, nullable=False)
