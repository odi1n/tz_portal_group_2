from fastapi import FastAPI

from src.routers import router

app = FastAPI(
    title="Tz portal group",
    version="0.1.0",
    description="Description api",
)
app.include_router(router)