"""
API Endpoints to support action and memory of reminder app

You can run it using `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

You can reach these API endpoints using http://211.216.235.50:30000/
3000 is mapped to 8000 (internally)
"""

from fastapi import FastAPI, HTTPException
import httpx
import asyncio
from mem0 import MemoryClient  # type: ignore
from typing import List
from app.models import Message, StorePromptsResponse, ReminderRegisterRequest


MEM0_API = "m0-g8dVJshuubNC8Vh3u3WF8kca5Ikkpy1D0vOfqkYj"
MEM0_USER = "hansu"

mem0_client = MemoryClient(api_key=MEM0_API)
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/store-prompts")
async def store_prompts(prompts: List[Message]):
    """
    Accepts a prompt and stores it in an external vector database via an API call.
    """
    print(prompts)
    messages = [message.model_dump() for message in prompts]
    print(messages)
    try:
        res = await asyncio.to_thread(
            mem0_client.add, messages, user_id=MEM0_USER, output_format="v1.1"
        )
        return StorePromptsResponse(
            status="success", message="Prompts stored successfully.", data=res
        )
    except Exception as e:
        print(f"Error storing prompts: {e}")
        raise HTTPException(status_code=500, detail="Failed to store prompts.") from e


@app.post("/register-reminder")
async def register_reminder(req: ReminderRegisterRequest):
    # print(req)
    request = req.model_dump()
    print(request)


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    await asyncio.sleep(5)
    return {"item_id": item_id, "query": q}


@app.get("/external-data")
async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
    data = response.json()
    return {"external_data": data}
