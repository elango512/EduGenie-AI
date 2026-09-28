from gemini_client import generate_content


def summarize_text(text: str) -> str:

    prompt = f"""
You are EduGenie, an AI educational assistant.

Summarize the following text for a college student.

Text:
{text}

Instructions:
- Keep the summary concise.
- Keep the important information.
- Use simple English.
- Do not change the meaning.
- Use a short heading.
- Use bullet points where appropriate.
"""

    return generate_content(prompt)