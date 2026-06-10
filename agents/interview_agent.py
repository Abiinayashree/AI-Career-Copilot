from models.llm_config import generate_response

def generate_interview_questions(skills, goal):

    prompt = f"""
    Current Skills:
    {skills}

    Career Goal:
    {goal}

    Generate:

    1. Technical Interview Questions
    2. HR Interview Questions
    3. Scenario-Based Questions
    4. Preparation Tips

    Keep the response structured.
    """

    return generate_response(prompt)