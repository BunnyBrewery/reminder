"""
Database: Postgresql

brew services list
brew services start postgresql

psql postgres

backslash l : list of databases 
backslash du : list of roles
"""

import asyncpg  # type: ignore
import os
from fastapi import HTTPException

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://hansulee:1234@localhost/reminder_db"
)


async def connect_to_db():
    try:
        return await asyncpg.connect(
            user="hansulee",
            password="1234",
            database="reminder_db",
            host="127.0.0.1",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


async def close_db_connection(connection):
    await connection.close()


class Database:
    """
    Hanlder class for DB connection.
    """

    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(DATABASE_URL)

    async def disconnect(self):
        await self.pool.close()

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                return await connection.execute(query, *args)

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)


db = Database()
