# nl-query-to-sparql

![CI Tests](https://github.com/tdiprima/nl2sparql/actions/workflows/ci.yml/badge.svg)

LLM SPARQL Query Testing

---

### **📌 How to Use**
1️⃣ Clone the repository:

   ```sh
   git clone https://github.com/tdiprima/nl2sparql/.git
   cd nl2sparql
   ```

2️⃣ Install dependencies:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3️⃣ Run tests:

   ```sh
   python -m unittest discover tests
   ```

4️⃣ Try out a **natural language query**:

   ```python
   from src.query_generator import generate_sparql
   print(generate_sparql("List all Nobel Prize winners in Physics after 2000."))
   ```

---

### **📈 Future Roadmap**
🛠️ **Improve SPARQL Accuracy:** Fine-tune query generation for better precision.  
🔍 **Support for Pathology Data:** Expand testing on **medical datasets** beyond DBPedia.  
📊 **User Interface:** Add a simple web or CLI-based UI for interactive query input.  
⚡ **Performance Optimizations:** Enhance query efficiency for larger datasets.  
