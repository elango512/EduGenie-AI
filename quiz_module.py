import json
import re

from gemini_client import generate_content


def clean_json_response(text: str) -> str:
    """
    Remove Markdown code fences if Gemini returns JSON inside them.
    """

    text = text.strip()

    text = re.sub(
        r"^```json\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^```\s*",
        "",
        text
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    return text.strip()


def validate_quiz(data):

    if not isinstance(data, list):
        raise ValueError("Quiz response must be a list.")

    if len(data) != 3:
        raise ValueError("Quiz must contain exactly 3 questions.")

    for question in data:

        if not isinstance(question, dict):
            raise ValueError("Invalid quiz question.")

        required_fields = [
            "question",
            "options",
            "answer"
        ]

        for field in required_fields:
            if field not in question:
                raise ValueError(
                    f"Missing field: {field}"
                )

        if not isinstance(question["options"], list):
            raise ValueError(
                "Options must be a list."
            )

        if len(question["options"]) != 4:
            raise ValueError(
                "Each question must have 4 options."
            )

    return data


def generate_quiz(topic: str):

    prompt = f"""
You are EduGenie, an AI quiz generator.

Create a quiz based on this topic:

{topic}

Create exactly 3 multiple-choice questions.

Each question must contain:
- question
- options
- answer

Each question must have exactly 4 options.

Return ONLY valid JSON.

Required format:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option A"
  }}
]

Do not add explanations outside the JSON.
"""

    response = generate_content(prompt)

    response = clean_json_response(response)

    try:
        data = json.loads(response)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Gemini returned invalid JSON: {error}"
        )

    return validate_quiz(data)