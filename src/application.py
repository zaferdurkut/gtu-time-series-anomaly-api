from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from src.api import common_controller, jpl_controller


def create_app():
    app = FastAPI(title="Time Series Anomaly Detector API",
                  description="Time Series Anomaly Detector API",
                  version="0.1.0",
                  openapi_url="/openapi.json",
                  docs_url="/",
                  redoc_url="/redoc"
                  )

    app.include_router(common_controller.router, prefix="/api/v1/common", tags=["common"])
    app.include_router(jpl_controller.router, prefix="/api/v1/jpl", tags=["common"])

    return app
