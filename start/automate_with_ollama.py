"""
Try it with Ollama mistral, ollama3.1 now.
automate_queries.py, using OpenAI's gpt-4, is much better.

Author: tdiprima
"""

__author__ = 'tdiprima'

import requests
import ollama
import json

# DBPedia SPARQL Endpoint
DBPEDIA_SPARQL_URL = "https://dbpedia.org/sparql"


def generate_sparql_query(natural_language_query):
    """
    Uses Ollama to generate a SPARQL query based on a natural language question, ensuring DBpedia compatibility.
    """
    prompt = (
        "Convert the following natural language question into a valid SPARQL query for DBPedia. "
        "Ensure the query follows DBpedia's ontology standards. Use proper prefixes like dbo:, rdf:, dcterms:. "
        "Do NOT include explanations, only return the raw SPARQL query.\n\n"
        "Use rdf:type dbo:Person instead of wd:Person. Ensure prefixes are properly declared. "
        f"Question: {natural_language_query}\nSPARQL Query:"
    )

    # Tried llama3.1 too.
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    response_text = response['message']['content']

    # Cleanup Ollama's output quirks
    response_text = response_text.replace('\n', ' ').replace('\\', '')
    response_text = response_text.strip('`')  # Remove potential markdown artifacts

    # Ensure necessary prefixes exist
    # if "PREFIX dbo:" not in response_text:
    #     response_text = "PREFIX dbo: <http://dbpedia.org/ontology/>\n" + response_text
    # if "PREFIX rdf:" not in response_text:
    #     response_text = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" + response_text
    # if "PREFIX dcterms:" not in response_text:
    #     response_text = "PREFIX dcterms: <http://purl.org/dc/terms/>\n" + response_text

    return response_text.strip()


def run_sparql_query(sparql_query):
    """
    Sends a SPARQL query to the DBPedia endpoint and retrieves the results.
    """
    params = {
        "query": sparql_query,
        "format": "application/json"
    }
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(DBPEDIA_SPARQL_URL, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"SPARQL query failed with status {response.status_code}"}


def main():
    """
    Main function to process a natural language question, convert it to SPARQL, and fetch results.
    """
    natural_query = "Who are some famous pathologists?"

    print("Generating SPARQL query...")
    sparql_query = generate_sparql_query(natural_query)
    print(f"Generated Query:\n{sparql_query}\n")

    print("Executing SPARQL query...")
    results = run_sparql_query(sparql_query)

    print("Results:")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
