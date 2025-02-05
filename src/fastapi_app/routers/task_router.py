from fastapi import APIRouter, Depends

from depends import authenticate, update_task, delete_task_, create_user_task, get_task_by_id, get_tasks_by_user_id
from schemas.task_schem import CreateTask, GetTask

router = APIRouter(
    prefix='/task',
    tags=['task']
)


@router.get('/{task_id}')
async def get_task(
    task_id: int,
    user_id: int = Depends(authenticate),
):
    res = await get_task_by_id(task_id)
    return res


@router.get('/all')
async def get_all_tasks(
    user_id: int = Depends(authenticate)
):
    res = await get_tasks_by_user_id(user_id)
    return res


@router.post('/create')
async def create_task(
    task: CreateTask,
    user_id: int = Depends(authenticate),
):
    res = await create_user_task(user_id, task)
    return res


@router.patch('/{task_id}')
async def patch_task(
    task_id: int,
    task_update: CreateTask,
    user_id: int = Depends(authenticate)
):
    res = await update_task(task_id, user_id, task_update)
    return res


@router.delete('/{task_id}')
async def delete_task(
    task_id: int,
    user_id: int = Depends(authenticate)
):
    res = await delete_task_(task_id, user_id)
    return res
