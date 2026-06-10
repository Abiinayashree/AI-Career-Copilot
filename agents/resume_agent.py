from models.llm_config import generate_response

def analyze_resume(resume_text, goal):

    prompt = f"""
    Resume:
    {resume_text}

    Career Goal:
    {goal}

    Analyze the resume and provide:

    1. Resume Strengths
    2. Areas for Improvement
    3. Missing Skills
    4. ATS Optimization Tips
    5. Suggested Projects

    Keep the response clear and structured.
    """

    return generate_response(prompt)

    