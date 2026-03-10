import os
from dotenv import load_dotenv
from groq import Groq
from settings import GROQ_API_KEY

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def correct_sentence(text):

    prompt = f"""
Correct the spelling and grammar of the sentence below.
Return ONLY the corrected sentence.

Sentence: {text}
"""

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        corrected = response.choices[0].message.content.strip()
        return corrected

    except Exception as e:
        print("AI Error:", e)
        return text