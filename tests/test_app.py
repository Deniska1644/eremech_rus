import asyncio
import json
import pytest
import httpx
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from config import settings

pytestmark = pytest.mark.asyncio


@pytest.mark.asyncio
class TestAuthHandlers:
    TEST_USER = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }

    def setup_method(self):
        self.host = 'localhost'
        self.port = 8000
        self.name = 'user'
        self.url = f'http://{self.host}:{self.port}/{self.name}'
        self.engine = create_async_engine(settings.get_pg_url())
        self.async_session_maker = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False)

    @pytest.mark.asyncio
    async def test_registrate_user(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(f'{self.url}/registrate', json=self.TEST_USER)
            assert response.status_code == 200
            assert response.json().get('status') == 'successful'

    @pytest.mark.asyncio
    async def test_registrate_user_exist(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(f'{self.url}/registrate', json=self.TEST_USER)
            assert response.status_code == 409
            assert response.json().get('detail') == 'user or email already exist'


@pytest.mark.asyncio
class TestTaskHandlers:
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

    def setup_method(self):
        self.host = 'localhost'
        self.port = 8000
        self.name = 'task'
        self.url = f'http://{self.host}:{self.port}/{self.name}'
        self.auth = httpx.BasicAuth(
            username=self.TEST_USER['username'], password=self.TEST_USER['password'])
        self.task_id = None

    @pytest.mark.asyncio
    async def test_create_task(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(f'{self.url}/create', auth=self.auth, json=self.TEST_TASK)
            assert response.status_code == 200
            assert response.json().get('status') == 'successful'
            self.task_id = response.json().get('id')
            print(response.json().get('id'))
            assert self.task_id is not None

    async def test_get_task(self, created_task):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'{self.url}/{created_task}/get', auth=self.auth)
            assert response.status_code == 200
            assert response.json().get('title') == self.TEST_TASK.get('title')
            assert response.json().get('description') == self.TEST_TASK.get('description')
            assert response.json().get('due_data') == self.TEST_TASK.get('due_data')

    async def test_get_all_tasks(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'{self.url}/all', auth=self.auth)
            assert response.status_code == 200

    async def test_update_task(self, created_task):
        async with httpx.AsyncClient() as client:
            response = await client.patch(f'{self.url}/{created_task}/update', auth=self.auth, json=self.TEST_TASK)
            assert response.status_code == 200
            assert response.json().get('status') == 'successful'

    async def test_delete_task(self, created_task):
        await asyncio.sleep(1)
        async with httpx.AsyncClient() as client:
            response = await client.delete(f'{self.url}/{created_task}/delete',  auth=self.auth)
            assert response.status_code == 200
            assert response.json().get('status') == 'successful'
