from fastapi import FastAPI
from app.middlewares import token
from app.base_router import v1_router

def initiate_app():
    app = FastAPI(
        title='Kafeku API V1 Documentation',
        description='Kafeku API V1 Documentation, made by gensart-x',
        version='1.0.0',

        redirect_slashes=False
    )

    # Middlewares
    app.add_middleware(token.BaseHTTPMiddleware)
    
    # Routes
    app.include_router(v1_router)
    return app