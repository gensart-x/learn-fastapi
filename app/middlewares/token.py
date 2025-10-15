from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from ..utils.http import is_whitelisted
import time

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        if is_whitelisted(request.url.path, ['/v1/desks']):
            return await call_next(request)
        
        print("[Timer] Before call_next")
        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time
        print("[Timer] After call_next")
        response.headers["X-Process-Time"] = str(process_time)
        return response


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("[Header] Before call_next")

        response = await call_next(request)

        print("[Header] After call_next")
        response.headers["X-Powered-By"] = "FastAPI"
        return response
