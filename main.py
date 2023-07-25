from fastapi import FastAPI
from app.routes.api import links

app = FastAPI()

app.include_router(links.router)
