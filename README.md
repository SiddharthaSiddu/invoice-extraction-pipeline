# Structured Data Extraction Pipeline

An enterprise-grade invoice processing system using Claude's tool_use to convert messy documents into strict, schema-validated JSON.

## 🛠️ Key Components
* **Tool-Based Extraction**: Uses a strict JSON schema with nullable fields to prevent data hallucinations.
* **Self-Correction & Math Validation**: Cross-checks line items against the stated total to flag errors.
* **Confidence Routing**: Automatically flags uncertain or low-confidence extractions for manual human review.
*