from gemini_client import generate_content


def recommend_learning_path(
    topic: str,
    level: str = "Beginner"
) -> str:

    prompt = f"""
You are EduGenie, an AI learning path advisor.

Create a personalized learning path.

Topic:
{topic}

Student Level:
{level}

Create a structured plan from basic to advanced.

Include:

1. Learning Goal
2. Prerequisites
3. Step-by-Step Learning Path
4. Practice Activities
5. Mini Projects
6. Suggested Resource Types
7. Expected Outcome

Use simple English.

Make the plan realistic for a college student.
"""

    return generate_content(prompt)