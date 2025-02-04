from SPARQLWrapper import SPARQLWrapper, JSON

# Define the SPARQL endpoint
DBPEDIA_ENDPOINT = "https://dbpedia.org/sparql"

# Define pathology-related SPARQL queries
QUERIES = {
    "Common Diseases": """
        SELECT ?disease ?description WHERE {
          ?disease rdf:type dbo:Disease .
          ?disease dbo:abstract ?description .
          FILTER (LANG(?description) = 'en')
        } LIMIT 10
    """,
    "Cancers and ICD-10 Codes": """
        PREFIX dct: <http://purl.org/dc/terms/>
        SELECT ?cancer ?label ?icd10 WHERE {
          ?cancer dct:subject dbc:Types_of_cancer .
          ?cancer rdfs:label ?label .
          OPTIONAL { ?cancer dbo:icd10 ?icd10 }
          FILTER (LANG(?label) = 'en')
        } LIMIT 10
    """,
    "Diseases and Associated Genes": """
        SELECT ?disease ?gene WHERE {
          ?disease rdf:type dbo:Disease .
          ?disease dbp:gene ?gene .
        } LIMIT 10
    """,
    "Liver Diseases": """
        PREFIX dct: <http://purl.org/dc/terms/>
        SELECT ?disease ?label WHERE {
          ?disease rdf:type dbo:Disease .
          ?disease dct:subject dbc:Hepatology .
          ?disease rdfs:label ?label .
          FILTER (LANG(?label) = 'en')
        } LIMIT 10
    """,
    "Pathology Scientists": """
        SELECT ?scientist ?name ?field WHERE {
          ?scientist rdf:type dbo:Scientist .
          ?scientist dbp:field dbr:Pathology .
          ?scientist foaf:name ?name .
          OPTIONAL { ?scientist dbo:academicDiscipline ?field }
          FILTER (LANG(?name) = 'en')
        } LIMIT 10
    """
}


def run_sparql_query(query):
    """Executes a SPARQL query against the DBPedia endpoint."""
    sparql = SPARQLWrapper(DBPEDIA_ENDPOINT)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    try:
        results = sparql.query().convert()
        return results.get("results", {}).get("bindings", [])
    except Exception as e:
        print(f"Error running query: {e}")
        return []


def display_results(title, results):
    """Formats and prints SPARQL query results."""
    print(f"\n🔬 {title}:")
    if not results:
        print("❌ No results found.")
        return

    for i, row in enumerate(results, start=1):
        print(', '.join(f"{k}: {v['value']}" for k, v in row.items()))


if __name__ == "__main__":
    print("🔍 Running pathology-related SPARQL queries on DBPedia...\n")
    for title, query in QUERIES.items():
        results = run_sparql_query(query)
        display_results(title, results)
