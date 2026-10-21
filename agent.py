import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors

from tools import search_web
from prompts import RESEARCH_REPORT_PROMPT

load_dotenv()

# The agent tries these models in order if one is busy
MODELS = ["gemini-flash-latest", "gemini-flash-lite-latest"]
WAIT_SECONDS = [5, 10, 20]


def ask_gemini(client, prompt):
    last_error = None

    for model_name in MODELS:
        for wait in WAIT_SECONDS:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                return response.text
            except errors.ServerError as error:
                last_error = error
                time.sleep(wait)

    raise last_error


def create_research_report(topic):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing. Add it to your .env file.")

    client = genai.Client(api_key=api_key)

    # 1. Search the web
    search_results = search_web(topic)

    # 2. Turn the results into text
    research_data = ""
    for result in search_results:
        research_data += f"""
TITLE: {result.get("title", "")}
URL: {result.get("url", "")}
CONTENT:
{result.get("content", "")}

----------------------------------------
"""

    # 3. Build the prompt
    prompt = RESEARCH_REPORT_PROMPT.format(
        topic=topic,
        research_data=research_data
    )

    # 4. Ask Gemini (with retries and a backup model)
    return ask_gemini(client, prompt)