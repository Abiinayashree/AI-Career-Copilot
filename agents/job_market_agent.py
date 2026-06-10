from models.llm_config import generate_response

def analyze_job_market(goal):

    prompt = f"""
    Career Goal:
    {goal}

    Provide:

    1. Top Skills in Demand
    2. Current Hiring Trends
    3. Based on general industry knowledge
    4. provide estimated trends.

    Keep the response structured.
    """

    return generate_response(prompt)