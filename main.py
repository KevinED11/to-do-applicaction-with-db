from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import status
from uvicorn import run as uvicorn_run
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from routers import tasks, users
from db import init_db
from dependencies import BASE_URL_APP
from tags import Tags


app = FastAPI(
    docs_url=BASE_URL_APP + "docs/",
    redoc_url=BASE_URL_APP + "redoc/",
)


origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=100)


@app.on_event("startup")
async def startup_event() -> None:
    # init_db()
    ...


@app.on_event("shutdown")
async def shutdown_event() -> None:
    ...


@app.get("/", tags=[Tags.ROOT])
async def read_root():
    return JSONResponse(content="Hello world", status_code=status.HTTP_200_OK)


app.include_router(router=tasks)


if __name__ == "__main__":
    uvicorn_run(app=app, host="0.0.0.0", port=8000)
