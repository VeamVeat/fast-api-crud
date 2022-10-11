import os

from fastapi import Request, HTTPException


class MyMiddleware:

    async def __call__(self, request: Request, call_next):
        authorization_header = request.headers.get("authorization")

        if authorization_header != os.getenv('AUTHORIZATION'):
            raise HTTPException(status_code=404, detail="Invalid authorization header specified")

        response = await call_next(request)

        return response
