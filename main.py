"""
API Endpoints to support action and memory of reminder app

You can run it using `uvicorn main:app --reload`

You can reach these API endpoints using http://211.216.235.50:30000/
3000 is mapped to 8000 (internally)
"""

from fastapi import FastAPI

import httpx
import asyncio

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


# Define a dynamic path endpoint
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    await asyncio.sleep(5)
    return {"item_id": item_id, "query": q}


# New endpoint that makes an asynchronous external API call
@app.get("/external-data")
async def get_external_data():
    async with httpx.AsyncClient() as client:
        # Asynchronous GET request to external API
        response = await client.get("https://api.example.com/data")

    # Process and return the response from the external API
    data = response.json()
    return {"external_data": data}
