from fastapi import Request, HTTPException
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from dependencies import settings


class MyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        authorization_header = request.headers.get("authorization")

        if authorization_header != settings.AUTHORIZATION:
            raise HTTPException(status_code=403, detail="Invalid authorization header specified")

        return await call_next(request)
