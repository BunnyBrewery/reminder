"""
Initial Setup for the Database
"""

from app.db.database import db


async def run_sql_script(script_path):
    async with db.pool.acquire() as connection:
        with open(script_path, "r", encoding="utf-8") as file:
            sql = file.read()
            await connection.execute(sql)


async def run():
    await run_sql_script("initial_setup.sql")


if __name__ == "__main__":
    run()
