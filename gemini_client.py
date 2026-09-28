import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)


if not API_KEY:
    raise RuntimeError(
        "Gemini API key not found. "
        "Please add GEMINI_API_KEY to your .env file."
    )


client = genai.Client(api_key=API_KEY)


def generate_content(prompt: str) -> str:
    """
    Send a prompt to Google Gemini and return the generated text.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    if not response or not response.text:
        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return response.text.strip()