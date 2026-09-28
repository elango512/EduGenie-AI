from gemini_client import generate_content


def explain_concept(concept: str) -> str:

    prompt = f"""
You are EduGenie, an AI tutor.

Explain the following concept to a beginner.

Concept:
{concept}

Give the response in this format:

Meaning:
Give a simple meaning.

Easy Explanation:
Explain the concept in simple language.

Example:
Give one easy real-world or programming example.

Key Points:
- Point 1
- Point 2
- Point 3

Use simple English suitable for a college student.
"""

    return generate_content(prompt)