from src.pipeline.extractor import InvoiceExtractor
from src.pipeline.validator import DataValidator

def run_extraction_pipeline():
    print("=== Launching Structured Data Extraction Pipeline ===")
    
    extractor = InvoiceExtractor()
    validator = DataValidator()
    
    # Simulate extraction result
    mock_data = {
        "vendor": "TechSupply Co",
        "date": "2026-06-04",
        "line_items": [{"description": "GPU", "amount": 500}, {"description": "Cable", "amount": 20}],
        "total_amount": 520
    }
    
    # Run Validation Loop
    is_valid, msg = validator.validate_math(mock_data)
    print(f"Validation Check: {msg}")
    
    # Confidence Routing
    action = validator.route_by_confidence(0.95)
    print(f"Pipeline Action: {action}")
    print("=== Extraction Workflow Complete ===")

if __name__ == "__main__":
    run_extraction_pipeline()