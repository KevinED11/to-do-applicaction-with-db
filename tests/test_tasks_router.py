from main import app
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse
from fastapi import status
from models.task import Task
from enum import StrEnum


client = TestClient(app)


class TasksRouterRoutes(StrEnum):
    ROOT = "http://localhost:8000/"
    TASKS = f"http://localhost:8000/api/v1/tasks"
    CREATE = "http://localhost:8000/api/v1/tasks/create"
    SEARCH_BY_ID = "http://localhost:8000/api/v1/tasks/{id}/".format(id=4)
    DELETE = "http://localhost:8000/api/v1/tasks/delete/{id}/".format(id=2)
    UPDATE = "http://localhost:8000/api/v1/tasks/update/{id}/".format(id=5)
    FILTER = "http://localhost:8000/api/v1/tasks/filter/{query}".format(
        query="?priority=10"
    )


print(list([client.get(TasksRouterRoutes.SEARCH_BY_ID).json()]))


class TestTasksRouter:
    @classmethod
    def setup_class(cls):
        cls.tasks_response = client.get(TasksRouterRoutes.TASKS)
        cls.search_response = client.get(TasksRouterRoutes.SEARCH_BY_ID)

    def test_read_root(self) -> None:
        response = client.get(TasksRouterRoutes.ROOT)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == "Hello world"

    def test_tasks(self) -> None:
        tasks = self.tasks_response.json()

        assert self.tasks_response.status_code == status.HTTP_200_OK
        assert len(tasks) == 10

        assert isinstance(tasks, list)
        assert tasks[0] == {
            "id": 1,
            "description": "my name is kevin",
            "created_at": "2023-06-23T22:55:35.165267",
            "state": "pending",
            "category_id": None,
            "title": "bañarme",
            "priority": 8,
        }

        for task in tasks:
            assert isinstance(Task(**task), Task)

    def test_search_by_id(self) -> None:
        task = self.search_response.json()

        assert self.search_response.status_code == status.HTTP_200_OK
        assert len(list([task])) == 1
        assert task == {
            "id": 4,
            "description": "stringstringstr",
            "created_at": "2023-06-23T23:25:01",
            "state": "pending",
            "category_id": None,
            "title": "string",
            "priority": 10,
        }

        # Expected keys in json response
        assert set(task.keys()) == {
            "id",
            "description",
            "created_at",
            "state",
            "category_id",
            "title",
            "priority",
        }

        assert isinstance(Task(**task), Task)

    def test_delete(self) -> None:
        response = client.delete(TasksRouterRoutes.DELETE)


print(TasksRouterRoutes.SEARCH_BY_ID.format(id=1))
