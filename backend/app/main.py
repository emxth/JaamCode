from fastapi import FastAPI

from app.core.config.settings import settings
from app.core.exceptions.handlers import install_exception_handlers
from app.core.logging.logger import configure_logging
from app.core.middleware.request_id import RequestIdMiddleware


def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

    app.add_middleware(RequestIdMiddleware)

    install_exception_handlers(app)

    @app.get("/health", tags=["system"])
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
