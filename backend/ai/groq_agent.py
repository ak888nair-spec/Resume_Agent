import os
import json

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise Exception("GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
You are an HR Resume Parser.

Return ONLY one valid JSON object.

Rules:
- Output must start with {
- Output must end with }
- No markdown.
- No explanations.
- No code fences.
- Every object and array must be valid JSON.
- If information is missing, use an empty string "" or an empty array [].

Schema:

{
  "name":"",
  "email":"",
  "phone":"",
  "linkedin":"",
  "github":"",
  "portfolio":"",
  "location":"",
  "summary":"",
  "education":[],
  "experience":[],
  "skills":[],
  "projects":[],
  "certifications":[],
  "languages":[],
  "achievements":[]
}
"""


def process_resume(text):

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                    "role": "user",
                "content": text
            }
        ],
        temperature=0,
        response_format={"type": "json_object"}
    )

    response = completion.choices[0].message.content.strip()

    print("\n========== GROQ RAW RESPONSE ==========\n")
    print(response)
    print("\n=======================================\n")

    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    try:
        return json.loads(response)

    except Exception:

        start = response.find("{")
        end = response.rfind("}")

        if start != -1 and end != -1:
            return json.loads(response[start:end+1])

        raise Exception("Groq did not return valid JSON.")