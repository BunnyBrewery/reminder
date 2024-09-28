"""
Storing models for Pydantic
"""

from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    role: str
    content: str


class ReminderRegisterRequest(BaseModel):
    type: str
    time_at_request_utc: str
    time_after_minutes: int
    time_after_hours: int
    cycle: str
    todo_message: str


class Messages(BaseModel):
    all: List[Message]


class StorePromptsResponse(BaseModel):
    status: str
    message: str
    data: dict
