from fastapi import APIRouter

from .v1.routes.users import user_router
from .v1.routes.desks import desk_router

v1_router = APIRouter(
    prefix='/v1',
    )
v1_router.include_router(user_router, prefix='/users')
v1_router.include_router(desk_router, prefix='/desks')