from fastapi import FastAPI
from app.base_router import v1_router

app = FastAPI(
    title='Kafeku API V1 Documentation',
    description='Kafeku API V1 Documentation, made by gensart-x',
    version='1.0.0',
    # openapi_tags=['3.2'],

    redirect_slashes=False
)

app.include_router(v1_router)
