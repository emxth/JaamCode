from fastapi import Depends, Request

from app.core.database.session import get_db


def get_request_id(request: Request) -> str:
    return getattr(request.state, "request_id", "")


DbSessionDep = Depends(get_db)
