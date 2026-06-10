from models.llm_config import generate_response

def match_jobs(skills, goal):

    prompt = f"""
    Current Skills:
    {skills}

    Career Goal:
    {goal}

    Suggest:

    1. Suitable Job Roles
    2. Required Skills
    3. Career Recommendations
    4. Entry-Level Job Opportunities

    Keep the response structured.
    """

    return generate_response(prompt)