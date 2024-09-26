from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

base_prompt = """Complete the following json format by reading the prompt given to you (do not return any text other json)

            (read my comments in json so that you can pick the right one or produce the right text):

                fill out this json below based on the above!
                {
                    "type": // choose between "reminder", "learning", "quote", "list"
                    "to do": // choose between "call", "send message", "sound alarm"
                    "time": // the actual time requests (you fill it out based on the prompt)
                    "items": // fill out the name of the medicine or at least related to what disease
                
                }

                    what I want to ask is here: 
        """


def load_env():
    load_dotenv()
    api_key = os.getenv("SECRECT")
    org_id = os.getenv("ORGANIZATION_ID")
    proj_id = os.getenv("PROJECT_ID")
    return api_key, org_id, proj_id


def get_openai_client():
    api_key, _, _ = load_env()
    client = OpenAI(api_key=api_key)
    return client


def transcript_audio(audio_path, openai_client, model="whisper-1") -> str:
    audio_file = open(audio_path, "rb")
    transcription = openai_client.audio.transcriptions.create(
        model=model, file=audio_file
    )
    return transcription.text


def main():
    client = get_openai_client()
    text = transcript_audio("output.wav", client)
    prompt = base_prompt + text
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    print(completion)
    print(completion.choices[0].message)


if __name__ == "__main__":
    main()

    # api_key, _, _ = load_env()
    # headers = {"Authorization": f"Bearer {api_key}"}
    # url = "https://api.openai.com/v1/completions"
    # data = {"model": "gpt-3.5-turbo", "prompt": prompt}
    # res = requests.post(url, headers=headers, data=data).json()
    # print(res)
