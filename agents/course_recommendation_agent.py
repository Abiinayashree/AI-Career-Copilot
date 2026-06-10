from models.llm_config import generate_response

def recommend_courses(skills, goal):

    prompt = f"""
    Current Skills:
    {skills}

    Career Goal:
    {goal}

    Suggest:

    1. Best Courses
    2. Documentation Links
    3. YouTube Resources
    4. Learning Order

    Keep response structured.
    """

    return generate_response(prompt)