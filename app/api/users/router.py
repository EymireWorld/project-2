from fastapi import APIRouter, Query

from app.dependencies import session_dep
from app.schemas import UserShowSchema

from . import services


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('')
async def get_users(
    session: session_dep,
    limit: int = Query(10, ge=5, le=100),
    offset: int = Query(0, ge=0)
) -> list[UserShowSchema]:
    return await services.get_users(session, limit, offset)  # type: ignore


@router.get('/{user_id}')
async def get_user(
    session: session_dep,
    user_id: int
) -> UserShowSchema:
    return await services.get_user(session, user_id)
