from fastapi import Request, HTTPException

from dependencies import settings


class MyMiddleware:

    async def __call__(self, request: Request, call_next):
        authorization_header = request.headers.get("authorization")

        if authorization_header != settings.AUTHORIZATION:
            raise HTTPException(status_code=403, detail="Invalid authorization header specified")

        response = await call_next(request)

        return response
