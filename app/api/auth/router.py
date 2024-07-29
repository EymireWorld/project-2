from fastapi import APIRouter

from app.dependencies import current_user_dep, session_dep
from app.schemas import (
    TokenSchema,
    UserShowSchema,
    UserSingInSchema,
    UserSingUpSchema
)

from . import services


router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post(
    '/sign_in',
    tags=['Auth']
)
async def sign_in(
    session: session_dep,
    data: UserSingInSchema
) -> TokenSchema:
    return await services.sing_in(session, data)


@router.post(
    '/sign_up',
    tags=['Auth']
)
async def sign_up(
    session: session_dep,
    data: UserSingUpSchema
) -> TokenSchema:
    return await services.sing_up(session, data)


@router.get(
    '/me',
    tags=['Auth']
)
async def profile(current_user: current_user_dep) -> UserShowSchema:
    return current_user  # type: ignore