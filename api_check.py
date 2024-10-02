"""
Test FastAPI endpoints
"""

import httpx
import asyncio


async def test_store_prompts():
    messages = [
        {"role": "user", "content": "I like to walk."},
        {"role": "user", "content": "I run nearly every day."},
    ]
    print("is running..")

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://211.216.235.50:30000/store-prompts", json=messages
        )
    print(response)
    print(response.status_code)
    # print(response.json())


async def test_register_reminder():
    reminder_data = {
        # pylint: disable=line-too-long
        # "reminder_repetition_type", choose one among one_time, daily, specific_days_of_week
        "reminder_repetition_type": "daily",
        # "days", if reminder_repetition_type is specific_days_of_week, put the days user mentioned here like ['mon', 'wed', 'sun']. Otherwise, put empty list. Days shouldn't be duplicated.
        "days": [],
        # "reminder_type", choose one among taking_medicine, morning_call, shopping_list, other_reminder,
        "reminder_type": "taking_medicine",
        # "time_at_request_utc", the exact time the reminder request was made
        "time_at_request_utc": "2024-09-28T12:00:00Z",
        # "relative_time", use this only when reminder_repetition_type is one_time AND user said 'after x minutes, x hours, or so on'.
        "relative_time": False,
        # "time_after_minutes", should be 0 is relative_time is false
        "time_after_minutes": 30,
        # "time_after_hours", should be 0 is relative_time is false
        "time_after_hours": 1,
        # "absolute_time", set this to True only when reminder_repetition_type is not one_time. If reminder_repetition_type is not one_time, then set it False
        "absolute_time": True,
        #  "todo_message", write here what user wanted to do, so that you can tell the user exaclty what they wanted.
        # "todo_message", don't write time and days or other such information. Only write things related to the specific activity.
        "todo_message": "Remind me to go to the shopping center at Coles",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://211.216.235.50:30000/register-reminder",
            json=reminder_data,
            timeout=120,
        )
    print(response)
    print(response.status_code)


# Run the test
asyncio.run(test_register_reminder())
