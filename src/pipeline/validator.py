class DataValidator:
    def validate_math(self, extracted_data):
        """Pass 3: Self-correction logic to ensure sums match."""
        stated_total = extracted_data.get("total_amount", 0)
        calculated_total = sum(item["amount"] for item in extracted_data.get("line_items", []))
        
        if abs(stated_total - calculated_total) > 0.01:
            return False, f"Math Mismatch: Stated {stated_total}, Calculated {calculated_total}"
        return True, "Math Validated"

    def route_by_confidence(self, confidence_score):
        """Pass 7: Routes to human if confidence is below threshold."""
        if confidence_score < 0.85:
            return "ROUTE_TO_HUMAN"
        return "PROCESS_AUTOMATICALLY"