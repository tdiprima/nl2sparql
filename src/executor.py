"""
Execute SPARQL Queries
"""
from SPARQLWrapper import SPARQLWrapper, JSON


def run_sparql_query(query):
    endpoint = "https://dbpedia.org/sparql"
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


if __name__ == "__main__":
    test_query = "SELECT ?name WHERE { ?person a dbo:Scientist . ?person dbo:award dbr:Nobel_Prize . ?person foaf:name ?name } LIMIT 10"
    print(run_sparql_query(test_query))
