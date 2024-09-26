from mem0 import MemoryClient

client = MemoryClient(api_key="m0-g8dVJshuubNC8Vh3u3WF8kca5Ikkpy1D0vOfqkYj")


# messages = [
#     {
#         "role": "user",
#         "content": "Hi, I'm Hansu. Remind me to take thyroid pill every even day. That is, check the date and if the day of the month is even, remind me to take the medicine early in the morning.",
#     },
#     {
#         "role": "assistant",
#         "content": "Hi, Hansu! I'm your assistant. I'll remember to remind you to take your thyroid medicine at around 10AM in the morning in every even day.",
#     },
# ]

# The default output_format is v1.0
# client.add(messages, user_id="alex", output_format="v1.0")

# To use the latest output_format, set the output_format parameter to "v1.1"
# client.add(messages, user_id="alex", output_format="v1.1")

query = "What are the things that I need to remind Hansu on 22/SEP/2024, especially in the morning?"


# To use the latest output_format, set the output_format parameter to "v1.1"
filters = {
    "AND": [
        {"user_id": "alex"},
        {
            "agent_id": {
                "in": [
                    "health",
                ]
            }
        },
    ]
}


hehe = client.search(query, version="v2", filters=filters)


print(hehe)
