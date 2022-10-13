from fastapi import Request, status
from fastapi.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from dependencies import settings


class MyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        authorization_header = request.headers.get("authorization")

        if authorization_header != settings.AUTHORIZATION:
            return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content="Invalid authorization header specified")

        return await call_next(request)
