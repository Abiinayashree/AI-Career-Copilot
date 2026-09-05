from groq import Groq
import os
from dotenv import load_dotenv
from groq import RateLimitError

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except RateLimitError as e:
        return f"⚠️ Rate Limit Reached\n\n{str(e)}"

    except Exception as e:
        return f"❌ Error: {str(e)}"