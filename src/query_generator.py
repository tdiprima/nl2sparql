"""
Test LLM Query Generation
"""
from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_sparql(natural_query):
    prompt = f"Convert this into a SPARQL query:\n{natural_query}"
    response = client.chat.completions.create(
        model="gpt-4",  # Adjust model if needed
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    user_query = "List all Nobel Prize winners in Physics after 2000."
    print(generate_sparql(user_query))
