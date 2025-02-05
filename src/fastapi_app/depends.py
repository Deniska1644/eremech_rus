from asyncio import Task
from fastapi import Depends
from passlib.context import CryptContext
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from dao.connect import user_worcker, task_worcker
from exeptions import user_already_exist, user_not_found, task_not_found, incorrect_username_or_password
from schemas.user_schem import RegUser, GetUser
from schemas.task_schem import CreateTask, GetTask, ListTask
from models.model import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBasic()


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate(creds: HTTPBasicCredentials = Depends(security)):
    user: User = await user_worcker.get(
        filter_field='username',
        filter_value=creds.username
    )
    if user:
        pass_check = verify_password(creds.password, user.hashed_pass)
        if pass_check:
            return user.id
    raise incorrect_username_or_password


async def create_user(user: RegUser):
    hashed_pass = hash_password(user.password)
    res = await user_worcker.add(
        username=user.username,
        email=user.email,
        hashed_pass=hashed_pass
    )
    if res:
        return res
    raise user_already_exist


async def get_user_by_id(user_id: int) -> User:
    res = await user_worcker.get(
        filter_field='id',
        filter_value=user_id
    )
    if res:
        return GetUser.from_orm(res)
    raise user_not_found


async def create_user_task(user_id: int, task_info: CreateTask):
    res = await task_worcker.add(
        user_id=user_id,
        **task_info.dict()
    )
    if res:
        return res


async def get_task_by_id(task_id: int):
    res = await task_worcker.get(
        filter_field='id',
        filter_value=task_id
    )
    if res:
        return GetTask.from_orm(res)
    raise task_not_found


async def get_tasks_by_user_id(user_id: int):
    res = await task_worcker.get_all(
        filter_field='user_id',
        filter_value=user_id
    )
    if res:
        return [GetTask.from_orm(task) for task in res]
    return []


async def update_task(task_id: int, user_id: int, task_update: GetTask):
    res = await task_worcker.update_task(
        filter_field='id',
        filter_value=task_id,
        owner_id=user_id,
        **task_update.dict()
    )
    if res:
        return res
    raise task_not_found


async def delete_task_(task_id: int, user_id: int):
    res = await task_worcker.delete_task(
        filter_field='id',
        filter_value=task_id,
        owner_id=user_id
    )
    if res:
        return res
    raise task_not_found
