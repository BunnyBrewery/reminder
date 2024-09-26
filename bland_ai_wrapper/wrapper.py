"""
Wrapper functions for default BlandAI API
"""

import requests
from typing import Dict, Any, Optional


class BlandAIWrapper:
    """
    Wrapper for interacting with the BlandAI API.

    This class provides methods to make API calls, including
    starting and ending calls using the BlandAI service.

    Attributes:
        api_key (str): The API key for authenticating with the API.
    """

    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.call_url = "https://api.bland.ai/v1/calls"
        self.hold_url = "https://api.bland.ai/hold"
        self.headers = {
            "authorization": api_key,
            "Content-Type": "application/json",
        }

    def call_with_pathway(
        self,
        phone_number: str,
        task: str,
        pathway_id: str,
        start_node_id: str = "1",
        voice: str = "alexa",
        first_sentence: str = "",
        wait_for_greeting: bool = True,
        block_interruptions: bool = True,
        interruption_threshold: int = 110,
        model: str = "enhanced",
        temperature: float = 0.2,
        keywords: Optional[list[str]] = None,
        language: str = "en",
        timezone: str = "KR",
        request_data: None = None,
        retry_wait: int = 10,
        voicemail_action: str = "hangup",
        max_duration: int = 2,
        record: bool = True,
        answered_by_enabled: bool = True,
        timeout=5,
    ) -> Dict[str, Any]:
        if keywords is None:
            keywords = []

        payload: Dict[str, Any] = {
            "phone_number": phone_number,
            "task": task,
            "pathway_id": pathway_id,
            "start_node_id": start_node_id,
            "voice": voice,
            "first_sentence": first_sentence,
            "wait_for_greeting": wait_for_greeting,
            "block_interruptions": block_interruptions,
            "interruption_threshold": interruption_threshold,
            "model": model,
            "temperature": temperature,
            "keywords": keywords,
            # "pronunciation_guide": [{}],
            "language": language,
            # "timezone": timezone,
            "request_data": request_data,
            # "tools": [{}],
            # "dynamic_data": [{"dynamic_data[i].response_data": [{}]}],
            # "start_time": "",  # immediate
            "retry": {"wait": retry_wait, "voicemail_action": voicemail_action},
            "max_duration": max_duration,
            "record": record,
            # "webhook": "<string>",
            # "webhook_events": ["<string>"],
            # "analysis_prompt": "<string>",
            # "analysis_schema": {
            #     "reminder_type": "string",
            #     "want_to_be_reminded": "boolean",
            #     "reminder_time": "YYYY-MM-DD HH:MM:SS",
            #     "repeated": "boolean",
            #     "cycle": "string",
            # },
            "answered_by_enabled": answered_by_enabled,
        }

        response: requests.Response = requests.request(
            "POST", self.call_url, json=payload, headers=self.headers, timeout=timeout
        )
        return response.json()

    # def hold(self, phone_number, hold_connect, task=None):
    #     data = {
    #         "phone_number": phone_number,
    #         "hold_connect": hold_connect,
    #         "task": task,
    #     }

    #     # Make the API call
    #     response = requests.post(url, json=data, headers=self.headers)

    #     # Return the response
    #     return response.json()

    def end_call(
        self, call_id: str, url="https://api.bland.ai/end", timeout=5
    ) -> Dict[str, Any]:
        data = {"call_id": call_id}
        response = requests.post(url, json=data, headers=self.headers, timeout=timeout)
        return response.json()
