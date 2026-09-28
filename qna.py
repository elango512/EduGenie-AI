from gemini_client import generate_content


def answer_question(question: str) -> str:

    prompt = f"""
You are EduGenie, an AI educational assistant.

Answer the student's question clearly and correctly.

Question:
{question}

Instructions:
- Use simple English.
- Explain for a college student.
- Keep the answer concise.
- Use examples when useful.
- Avoid unnecessary technical complexity.
- If the question needs steps, provide numbered steps.
"""

    return generate_content(prompt)