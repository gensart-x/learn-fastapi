from typing import Annotated
from fastapi import APIRouter, Body
from pydantic import BaseModel

user_router = APIRouter()

class User(BaseModel):
    name: Annotated[str, Body(
        description='Name of the user'
    )]
    age: Annotated[int, Body(
        description='Age of the user',
        gt=0,
        le=100
    )]
    address: Annotated[str | None, Body(
        description='Address of the user'
    )]
    
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'name': 'John Doe',
                    'age': 20,
                    'address': '123 Main St'
                }
            ]   
        }
    }

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

@user_router.post(
    '/',
    tags=['🧑 Users'],
    summary='Create a new user',
    description='Create a new user',
)
async def create_user(
    user: User
):
    return {
        'success': True,
        'data': user,
    }