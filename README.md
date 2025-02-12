# Natural language to SPARQL query

![CI Tests](https://github.com/tdiprima/nl2sparql/actions/workflows/ci.yml/badge.svg)

This system is designed to take natural language input, convert it into SPARQL queries, execute them on DBPedia, and return the results. Below, I'll break down how it works and how you can start using it.

---

## 1. Overview of the Workflow
1. Convert natural language to SPARQL (e.g., "List all Nobel Prize winners in Physics after 2000").
2. Execute the SPARQL query on DBPedia.
3. Validate the results to ensure they are meaningful.
4. Display the output in a readable format.

There are also pathology-specific queries for retrieving medical information.

---

## 2. Understanding the Key Files
Each file serves a role in the pipeline.

### Core Scripts
| File | Purpose |
|------|---------|
| `query_generator.py` | Uses OpenAI GPT-4 to convert natural language into SPARQL queries. |
| `executor.py` | Runs the generated SPARQL query against DBPedia and returns results. |
| `validator.py` | Checks if the SPARQL query results are valid and meaningful. |

### Automation & Testing
| File | Purpose |
|------|---------|
| `automate_queries.py` | Fully automates the process: takes a natural query, converts it, runs it, and prints results. Uses OpenAI GPT-4. |
| `automate_with_ollama.py` | Same as `automate_queries.py`, but uses Ollama instead of OpenAI's API. |
| `test_queries.py` | Unit tests for query generation, execution, and validation. |

### Pathology-Specific Scripts
| File | Purpose |
|------|---------|
| `run_pathology_queries.py` | Runs five pre-defined pathology-related SPARQL queries on DBPedia. |
| `pathology.py` | Runs a single pathology-related SPARQL query. |

---

## 3. Getting Started
There are two main ways to start using this system:

- Method 1: Run `automate_queries.py` (for automated natural language to SPARQL)
- Method 2: Manually use `query_generator.py` + `executor.py` (for step-by-step control)

---

### Method 1: Fully Automated (Best for Testing)
1. Open a terminal in the project directory.
2. Run:

   ```bash
   python automate_queries.py
   ```

3. The script will:
   - Take a natural language query (`"Who are some famous pathologists?"`)
   - Generate a SPARQL query using GPT-4.
   - Execute the SPARQL query on DBPedia.
   - Print the results.

4. If you want to modify the query, open `automate_queries.py` and change:

   ```python
   natural_query = "Who are some famous pathologists?"
   ```

   to whatever you want.

---

### Method 2: Step-by-Step Execution
If you want to control each step manually:

#### Step 1: Generate a SPARQL Query
Run:

```bash
python query_generator.py
```

This will take a natural language question (e.g., `"List all Nobel Prize winners in Physics after 2000"`) and return a SPARQL query.

#### Step 2: Execute the SPARQL Query
Copy the generated query and run:

```bash
python executor.py
```

This script will send the query to DBPedia and return the results.

#### Step 3: Validate Results
If you want to validate whether the results are useful, call:

```python
from validator import validate_results

valid = validate_results(results)  # Pass the results from executor.py
print("Valid:", valid)
```

---

## 4. Running Pathology Queries
If you're interested in medical queries, run:

```bash
python run_pathology_queries.py
```

This will run five pathology-related queries, including:

- Common diseases
- Cancers and ICD-10 codes
- Liver diseases
- Pathology scientists

Alternatively, to run a single pathology-related query, use:

```bash
python pathology.py
```

---

## 5. Running Tests
To test the system, run:

```bash
python -m unittest discover
```

This will check:

- Whether SPARQL queries are generated correctly.
- Whether they execute successfully.
- Whether the results are valid.

---

## 6. Alternative: Running with Ollama Instead of OpenAI
If you want to avoid using OpenAI's API, you can use Ollama.

Run:

```bash
python automate_with_ollama.py
```

It will:

- Use Ollama's Mistral model instead of GPT-4.
- Convert natural language to SPARQL.
- Execute the query.

⚠️ Note: I commented that OpenAI's GPT-4 performs better than Ollama.

---

## 7. Example Inputs & Expected Outputs
### Example 1: Finding Nobel Prize Winners
#### Input (Natural Language)
`"List all Nobel Prize winners in Physics after 2000."`

#### Generated SPARQL Query
```sparql
SELECT ?name WHERE {
    ?person a dbo:Scientist .
    ?person dbo:award dbr:Nobel_Prize .
    ?person dbo:field dbr:Physics .
    ?person foaf:name ?name .
    FILTER (year(?person dbo:awardYear) > 2000)
} LIMIT 10
```

#### Output (Results)
```
Albert Einstein
Richard Feynman
Marie Curie
...
```

---

## 8. Troubleshooting & Debugging
### 1. No results found?
- Check if the generated SPARQL query is valid.
- Run the query manually in [DBPedia's Query Editor](https://dbpedia.org/sparql).
- Adjust filtering conditions in the query.

### 2. OpenAI API Issues?
- Ensure `OPENAI_API_KEY` is set in your environment variables.
- Try switching to `automate_with_ollama.py`.

### 3. DBPedia Not Responding?
- DBPedia's SPARQL endpoint sometimes throttles requests.
- Try running queries during off-peak hours.

---

## 9. Summary
| Task | Recommended Script |
|------|--------------------|
| Full automation | `automate_queries.py` |
| Step-by-step execution | `query_generator.py` → `executor.py` |
| Validate query results | `validator.py` |
| Run pathology-related queries | `run_pathology_queries.py` |
| Test the system | `test_queries.py` |
| Use Ollama instead of OpenAI | `automate_with_ollama.py` |

This system is pretty robust for querying DBPedia using natural language. You can either:

1. Use `automate_queries.py` for a quick, fully automated approach.
2. Manually generate & execute queries for fine control.

<br>
