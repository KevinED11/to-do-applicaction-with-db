from typing import TypedDict
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware


class Middlewares(TypedDict):
    ...


MIDDLEWARES = []
