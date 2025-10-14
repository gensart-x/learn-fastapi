from fastapi import APIRouter

desk_router = APIRouter()


@desk_router.get('/', tags=['🪑 Desks'])
async def get_desks():
    return {
        'success': True,
        'data': [],
    }
