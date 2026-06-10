from models.llm_config import generate_response

def career_chatbot(user_question):

    prompt = f"""
    You are an AI Career Coach.

    User Question:
    {user_question}

    Give professional career guidance,
    learning advice,
    interview tips,
    project suggestions,
    and roadmap recommendations.

    Keep the response structured.
    """

    return generate_response(prompt)