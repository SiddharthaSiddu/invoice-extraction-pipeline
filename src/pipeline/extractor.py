class InvoiceExtractor:
    def get_tool_definition(self):
        """Defines the strict JSON schema for tool_use."""
        return {
            "name": "extract_invoice",
            "description": "Extracts structured invoice data. Fields should be null if not found.",
            "parameters": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string"},
                    "date": {"type": "string", "description": "ISO 8601 format"},
                    "line_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "description": {"type": "string"},
                                "amount": {"type": "number"}
                            }
                        }
                    },
                    "total_amount": {"type": "number"}
                },
                "required": ["vendor", "total_amount"]
            }
        }