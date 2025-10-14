from fastapi import APIRouter

user_router = APIRouter()


@user_router.get(
    '/',
    tags=['🧑 Users'],
    summary='Get all users',
    description='Get all connected and disconnected users',
)
async def get_users():
    return {
        'success': True,
        'data': [],
    }
