"""
Natural language to SPARQL, query dbpedia, and return the results.
Modify "natural_query" in main()

Author: tdiprima
"""

__author__ = 'tdiprima'

from openai import OpenAI
import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# DBPedia SPARQL Endpoint
DBPEDIA_SPARQL_URL = "https://dbpedia.org/sparql"


def generate_sparql_query(natural_language_query):
    """
    Uses GPT to generate a SPARQL query based on a natural language question.
    """
    prompt = f"Convert the following natural language question into a SPARQL query for DBPedia:\n\nQuestion: {natural_language_query}\nSPARQL Query:"

    response = client.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])

    return response.choices[0].message.content.strip()


def run_sparql_query(sparql_query):
    """
    Sends a SPARQL query to the DBPedia endpoint and retrieves the results.
    """
    params = {"query": sparql_query, "format": "json"}
    response = requests.get(DBPEDIA_SPARQL_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def main():
    # Example natural language query
    natural_query = "Who are some famous pathologists?"

    # Generate SPARQL query
    sparql_query = generate_sparql_query(natural_query)
    print("\nGenerated SPARQL Query:\n", sparql_query)

    # Run SPARQL query
    results = run_sparql_query(sparql_query)

    if results:
        print("\nSPARQL Query Results:")
        for binding in results["results"]["bindings"]:
            print(binding)


if __name__ == "__main__":
    main()
