from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, insert, delete, create_engine, and_, update, delete
from sqlalchemy.exc import IntegrityError

from models.model import Base, User, Tasks
from config import settings


class DbConn:
    DATABASE_URL = settings.get_pg_url()

    def __init__(self):
        self.engine = create_async_engine(self.DATABASE_URL)
        self.async_session_maker = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False)


class DBWorcker(DbConn):
    def __init__(self, model):
        self.model = model
        super().__init__()

    async def add(self, **kwargs) -> bool:
        async with self.async_session_maker() as session:
            try:
                query = insert(self.model).values(
                    **kwargs).returning(self.model.id)
                res = await session.execute(query)
                _ = res.fetchone()
                print(res)
                await session.commit()

                return {'status': 'successful', 'id': _[0]}

            except IntegrityError as e:
                print(e)
                return False

    async def get(self, filter_field: str, filter_value: int | str):
        async with self.async_session_maker() as session:
            try:
                query = select(self.model).where(
                    getattr(self.model, filter_field) == filter_value)
                res = await session.execute(query)
                user = res.scalars().first()
                return user

            except IntegrityError as e:
                print(e)
                return False

    async def get_all(self, filter_field: str, filter_value: int | str):
        async with self.async_session_maker() as session:
            try:
                query = select(self.model).where(
                    getattr(self.model, filter_field) == filter_value
                )
                res = await session.execute(query)
                users = res.scalars().all()
                return users

            except IntegrityError as e:
                print(e)
                return False

    async def get_multifilter(self, first_filter: str, first_filter_value: str | int,
                              second_filter: str, second_filter_value: str | int):
        async with self.async_session_maker() as session:
            try:
                query = select(self.model).filter(
                    and_(getattr(self.model, first_filter)
                         == first_filter_value),
                    (getattr(self.model, second_filter) == second_filter_value))

                res = await session.execute(query)
                users = res.scalars().all()
                return users

            except IntegrityError as e:
                print(e)
                return False

    async def update_task(self, filter_field: str, filter_value: str | int, owner_id: int, **kwargs):
        async with self.async_session_maker() as session:
            try:
                query = update(self.model).filter(
                    and_(getattr(self.model, filter_field)
                         == filter_value),
                    (getattr(self.model, 'user_id') == owner_id)).values(**kwargs).returning(self.model.id)

                res = await session.execute(query)
                task = res.fetchone()
                await session.commit()
                if task:
                    return {'status': 'successful', 'id': task[0]}
                return False

            except IntegrityError as e:
                print(e)
                return False

    async def delete_task(self, filter_field: str, filter_value: str | int, owner_id: int):
        async with self.async_session_maker() as session:
            try:
                query = delete(self.model).filter(
                    and_(getattr(self.model, filter_field)
                         == filter_value),
                    (getattr(self.model, 'user_id') == owner_id)).returning(self.model.id)

                await session.execute(query)
                await session.commit()
                return {'status': 'successful', 'id': filter_value, 'operation': 'delete'}

            except IntegrityError as e:
                print(e)
                return False


user_worcker = DBWorcker(User)
task_worcker = DBWorcker(Tasks)
