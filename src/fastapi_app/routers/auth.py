from fastapi import APIRouter, Depends

from schemas.user_schem import RegUser
from depends import create_user, get_user_by_id, authenticate


router = APIRouter(
    prefix='/user',
    tags=['auth']
)


@router.post('/registrate')
async def registrate(user: RegUser):
    res = await create_user(user)
    return res


@router.get('')
async def user_info(user_id: str = Depends(authenticate)):
    res = await get_user_by_id(user_id)
    return res
