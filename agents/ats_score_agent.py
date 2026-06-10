from models.llm_config import generate_response

def analyze_ats_score(resume_text, goal):

    prompt = f"""
    Resume Content:
    {resume_text}

    Career Goal:
    {goal}

    Analyze the resume and provide:

    1. Estimated ATS Compatibility Score
    2. Missing Keywords
    3. Resume Strengths
    4. Areas for Improvement
    5. Final Suggestions

    Keep the response structured.
    """

    return generate_response(prompt)