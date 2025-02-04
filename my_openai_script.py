import os

import openai
from openai import OpenAI

# Get API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set! Check your GitHub Actions secret.")

print("API Key successfully retrieved (masked in logs)")

openai.api_key = api_key  # Explicitly set the API key

response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello, AI!"}])

print(response)
