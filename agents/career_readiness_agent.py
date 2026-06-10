from models.llm_config import generate_response

def analyze_career_readiness(skills, goal):

    prompt = f"""
    Current Skills:
    {skills}

    Career Goal:
    {goal}

    Analyze and provide:

    1. Career Readiness Score (out of 100)
    2. Strong Skills
    3. Missing Skills
    4. Estimated Learning Time
    5. Improvement Suggestions

    Keep the response structured.
    """

    return generate_response(prompt)