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


# Run the test
asyncio.run(test_store_prompts())
