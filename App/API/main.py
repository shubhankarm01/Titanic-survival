from fastapi import FastAPI, APIRouter, Request
from API.config import settings, setup_app_logging

from typing import Any

from fastapi.responses import HTMLResponse
from API.api import api_router
from fastapi.middleware.cors import CORSMiddleware

from loguru import logger

setup_app_logging(config = settings)

app = FastAPI(title = settings.PROJECT_NAME, openapi_url = f"{settings.API_V1_STR}/openapi.json")

root_router = APIRouter()

@root_router.get("/")
def index(request: Request) -> Any:
    body = (
        "<html>"
        "<body>"
        "<h1> Welcome </h1>"
        "<div> Check the docs: <a href = '/docs' </a> docs </div>"
        "</body>"
        "</html>"
        )
    return HTMLResponse(content = body)

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware, 
        allow_origins = [str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"])
    
if __name__ == "__main__":
    
    logger.warning("Running in development mode. Do not run like this in production.")
    
    import uvicorn
    uvicorn.run(app, host = "localhost", port = 8001, log_level = "debug")