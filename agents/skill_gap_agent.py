from models.llm_config import generate_response

def analyze_skill_gap(skills, goal):

    prompt = f"""
    Current Skills:
    {skills}

    Career Goal:
    {goal}

    Analyze the skill gap.

    Return:

    1. Existing Skills
    2. Missing Skills
    3. Importance of Missing Skills

    Keep the response clear and structured.
    """

    return generate_response(prompt)

    