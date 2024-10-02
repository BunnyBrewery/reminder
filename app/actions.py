"""
Reads todos from the database. And take actions.
"""

from app.db.database import db
from fastapi import HTTPException


async def read_reminders_from_db():
    query = "SELECT * FROM reminder_list;"
    try:
        reminders = await db.fetch(query)
        return reminders
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching reminders: {e}"
        ) from e


def take_action():
    pass


if __name__ == "__main__":
    res = read_reminders_from_db()
    print(res)
