from models.llm_config import generate_response

def analyze_linkedin_profile(profile_text):

    prompt = f"""
    LinkedIn Profile Summary:
    {profile_text}

    Analyze and provide:

    1. Profile Strength Score
    2. Missing Keywords
    3. Headline Improvements
    4. Profile Optimization Tips
    5. Recruiter Visibility Suggestions

    Keep the response structured.
    """

    return generate_response(prompt)