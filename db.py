from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy.engine import Engine
# from models.category import Category, CategoryEnum
# from models.task import Task, TaskEnum
from models import Category, Task, TaskEnum, CategoryEnum
import datetime


def conn(filename: str = "database.db") -> Engine:
    return create_engine(f"sqlite:///{filename}", echo=True)


engine = conn()


def create_tables() -> None:
    SQLModel.metadata.create_all(bind=engine)


def create_tasks() -> None:
    # category1 = Category(type=CategoryEnum.OTHER)
    task1 = Task(
        title="bañarme",
        priority=8,
        created_at=datetime.datetime.now(),
        description="my name is kevin", 
        state=TaskEnum.PENDING,
       # category_id=category1.id

    )

    with Session(engine) as session:
        session.add(task1)
        # session.add(category1)
        
        session.commit()


def create_categories() -> None:
    with Session(engine) as session:
         category1 = Category(type=CategoryEnum.PERSONAL)
         category2 = Category(type=CategoryEnum.WORK)
         category3 = Category(type=CategoryEnum.SHOPPING)
         category4 = Category(type=CategoryEnum.OTHER)
         
         session.add(category1)
         session.add(category2)
         session.add(category3)
         session.add(category4)
         
         session.commit()


def init_db() -> None:
    create_tables()
    create_tasks()
    create_categories()


if __name__ == "__main__":
    init_db()