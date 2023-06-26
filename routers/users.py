from fastapi import APIRouter
from typing import Annotated
from tags import Tags

users = APIRouter(prefix="/api/v1/users", tags=[Tags.USERS])


@users.get("/")
async def read_users():
    ...


@users.post("/create/")
async def create():
    ...


@users.patch("/update/{id}")
async def update(id: int):
    ...


@users.delete("/delete/{id}")
async def delete(id: int):
    ...
