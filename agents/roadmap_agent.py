from models.llm_config import generate_response

def generate_roadmap(skills, goal):

    prompt = f"""
    Current Skills:
    {skills}

    Career Goal:
    {goal}

    Create a 6-month learning roadmap.

    Format:

    Month 1:
    Month 2:
    Month 3:
    Month 4:
    Month 5:
    Month 6:

    Include:
    - Topics to learn
    - Mini projects
    - Important tools

    Keep it practical and beginner-friendly.
    """

    return generate_response(prompt)

    