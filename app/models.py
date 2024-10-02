"""
Storing models for Pydantic
"""

from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    role: str
    content: str


class ReminderRegisterRequest(BaseModel):
    reminder_repetition_type: str
    days: List[str]
    reminder_type: str
    time_at_request_utc: str
    relative_time: bool
    time_after_minutes: int
    time_after_hours: int
    absolute_time: bool
    todo_message: str


class ReminderResponse(BaseModel):
    status: str
    message: str


class Messages(BaseModel):
    all: List[Message]


class StorePromptsResponse(BaseModel):
    status: str
    message: str
    data: dict
