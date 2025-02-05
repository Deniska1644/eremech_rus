
import asyncio
import pytest
import httpx
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from config import settings

TEST_USER = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpassword"
}
TEST_TASK = {
    "title": "string",
    "description": "string",
    "due_data": "2025-02-05",
}

@pytest.fixture(scope='session')
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='module')
async def created_task():
    url = f'http://{settings.APP_HOST}:{settings.APP_PORT}/task'
    auth = httpx.BasicAuth(
            username=TEST_USER['username'], password=TEST_USER['password'])
    async with httpx.AsyncClient() as client:
        response = await client.post(f'{url}/create', auth=auth, json=TEST_TASK)
        return response.json().get('id')

