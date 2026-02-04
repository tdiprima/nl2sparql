"""
Query dbpedia with a pathology query.

Author: tdiprima
"""

__author__ = 'tdiprima'

import requests

# DBPedia SPARQL Endpoint
DBPEDIA_SPARQL_URL = "https://dbpedia.org/sparql"

# Your SPARQL Query
SPARQL_QUERY = """
SELECT ?disease ?description WHERE {
    ?disease rdf:type dbo:Disease .
    ?disease dbo:abstract ?description .
    FILTER (LANG(?description) = 'en')
} LIMIT 10
"""


def run_sparql_query(sparql_query):
    """
    Sends a SPARQL query to the DBPedia endpoint and retrieves the results.
    """
    params = {"query": sparql_query, "format": "json"}
    response = requests.get(DBPEDIA_SPARQL_URL, params=params, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def main():
    # Run the SPARQL query
    results = run_sparql_query(SPARQL_QUERY)

    if results:
        print("\nPathology-related Data in DBPedia:\n")
        for binding in results["results"]["bindings"]:
            disease = binding["disease"]["value"]
            description = binding["description"]["value"]
            print(f"Disease: {disease}\nDescription: {description}\n")


if __name__ == "__main__":
    main()
