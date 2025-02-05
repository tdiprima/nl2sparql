"""
Validate Query Results

Author: tdiprima
"""

__author__ = 'tdiprima'


def validate_results(results):
    if results and "results" in results:
        return len(results["results"]["bindings"]) > 0
    return False
