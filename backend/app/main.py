from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.middleware import request_tracking_middleware

setup_logging(settings.log_level)

app = FastAPI(
    title=settings.app_name,
    description="Agentic AI Reliability, Evaluation & Security Platform",
    version=settings.app_version,
    debug=settings.debug,
)

app.middleware("http")(request_tracking_middleware)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"],
)