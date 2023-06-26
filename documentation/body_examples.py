from _types import TaskBodyExample, CategoryBodyExample
from models.task import TaskEnum
from models.category import CategoryEnum




task_body_example  = TaskBodyExample(
    title="Sleep", description="Sleep for 8 hours", priority=10, state=TaskEnum.PENDING
)


category_body_example = CategoryBodyExample(type=CategoryEnum.WORK)
