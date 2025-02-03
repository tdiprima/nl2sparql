"""
Validate the query generation and execution
From root, execute: python -m unittest discover tests
"""
import unittest
from src.query_generator import generate_sparql
from src.executor import run_sparql_query
from src.validator import validate_results


class TestSPARQLQueries(unittest.TestCase):

    def test_sparql_generation(self):
        """Test if the LLM generates a valid SPARQL query from natural language."""
        natural_query = "List all Nobel Prize winners in Physics after 2000."
        sparql_query = generate_sparql(natural_query)

        self.assertIn("SELECT", sparql_query, "Generated query should contain SELECT")
        self.assertIn("WHERE", sparql_query, "Generated query should contain WHERE")

    def test_sparql_execution(self):
        """Test if a sample SPARQL query executes correctly on DBPedia."""
        sparql_query = """
        SELECT ?name WHERE { 
            ?person a dbo:Scientist . 
            ?person dbo:award dbr:Nobel_Prize . 
            ?person foaf:name ?name 
        } LIMIT 10
        """
        results = run_sparql_query(sparql_query)
        self.assertTrue(results, "SPARQL execution should return results")

    def test_results_validation(self):
        """Test if the result validation correctly identifies valid results."""
        results = {
            "head": {"vars": ["name"]},
            "results": {"bindings": [{"name": {"type": "literal", "value": "Albert Einstein"}}]}
        }
        self.assertTrue(validate_results(results), "Results validation should return True for valid results")

    def test_invalid_results(self):
        """Test validation with an empty result set."""
        results = {"head": {"vars": ["name"]}, "results": {"bindings": []}}
        self.assertFalse(validate_results(results), "Results validation should return False for empty results")


if __name__ == '__main__':
    unittest.main()
