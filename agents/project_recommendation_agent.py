from models.llm_config import generate_response

def recommend_projects(skills, goal):

    prompt = f"""
    Current Skills:
    {skills}

    Career Goal:
    {goal}

    Suggest:

    1. Portfolio Projects
    2. Difficulty Level
    3. Technologies Required
    4. Learning Benefits

    Keep the response structured.
    """

    return generate_response(prompt)