from fastapi import FastAPI
from app.middlewares import token
from app.base_router import v1_router

def initiate_app():
    app = FastAPI(
        title='Kafeku API V1 Documentation',
        description='Kafeku API V1 Documentation, made by gensart-x',
        version='1.0.0',

        redirect_slashes=True,
        openapi_url='/kafeku-openapi-1.0.0.json',
    )

    # Middlewares
    app.add_middleware(token.TimerMiddleware)
    app.add_middleware(token.CustomHeaderMiddleware)
    
    # Routes
    app.include_router(v1_router)
    return app