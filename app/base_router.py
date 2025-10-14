from fastapi import APIRouter, Depends
from .utils.http import verify_token

from .v1.routes.users import user_router
from .v1.routes.desks import desk_router

v1_router = APIRouter(
    prefix='/v1',
    dependencies=[Depends(verify_token)]
    )
v1_router.include_router(user_router, prefix='/users')
v1_router.include_router(desk_router, prefix='/desks')