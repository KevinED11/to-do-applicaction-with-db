from models.category import CategoryEnum
from pydantic import BaseModel, Field


class CategoryBody(BaseModel):
    category_type: CategoryEnum = Field(default=CategoryEnum.WORK)
