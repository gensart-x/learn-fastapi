from typing import Annotated
from fastapi import Header, HTTPException, status


async def verify_token(token: Annotated[str, Header(
    alias='Authorization',
    description='JWT token generated from the /login endpoint'
)]):
    if (token != 'secrecy'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token'
        )
