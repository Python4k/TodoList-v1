from sqlalchemy import insert, select, update
from .models import Todo
from app.database.db import async_session


async def get_todos():
    async with async_session() as session:
        query = select(Todo)
        result = await session.execute(query)
        return result.scalars().all()

async def get_todo_by_id(id):
    async with async_session() as session:
        query = select(Todo).where(Todo.id == id)
        result = await session.execute(query)
        return result.scalar()

async def create_todo(**kwargs):
    async with async_session() as session:
        query = insert(Todo).values(**kwargs)
        result = await session.execute(query)
        id = result.inserted_primary_key[0]
        await session.commit()
        return id


async def update_todo(id: int, **kwargs):
    async with async_session() as session:
        query = update(Todo).where(Todo.id == id).values(**kwargs)
        await session.execute(query)
        await session.commit()


async def delete_todo(id):
    async with async_session() as session:
        query = select(Todo).where(Todo.id == id)
        result = await session.execute(query)
        todo = result.scalar()
        await session.delete(todo)
        await session.commit()
