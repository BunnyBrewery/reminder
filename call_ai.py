"""
This module provides a basic sequence for making a call with a user
"""

from dotenv import load_dotenv
import os
from typing import Dict, Any, Tuple
from bland_ai_wrapper import BlandAIWrapper


def load_env() -> Tuple[str, str, str]:
    load_dotenv()

    api_key = os.getenv("API_KEY")
    pathway_id = os.getenv("PATHWAY_ID")
    target_number = os.getenv("TARGET_PHONE_NUMBER")

    if api_key is None:
        raise ValueError("API_KEY environment variable is not set.")
    if pathway_id is None:
        raise ValueError("PATHWAY_ID environment variable is not set.")
    if target_number is None:
        raise ValueError("TARGET_PHONE_NUMBER environment variable is not set.")

    return api_key, pathway_id, target_number


def main() -> None:
    api_key, pathway_id, target_number = load_env()
    task = (
        "Your name is Javis. You are here to help manage reminders and todo for the person. Listen to what they want to be reminded of, and confirm that you will remind them later for their request.",
    )
    bland_ai: BlandAIWrapper = BlandAIWrapper(api_key)
    response: Dict[str, Any] = bland_ai.call_with_pathway(
        phone_number=target_number, task=task[0], pathway_id=pathway_id
    )
    print(response)
    if response["status"] == "error":
        exit()

    call_id = response["call_id"]
    print(call_id)

    # end_call = bland_ai.end_call(call_id=call_id)
    # print(end_call)


if __name__ == "__main__":
    main()
