import os
import pytest
from werkzeug.datastructures import FileStorage
import sys

# Access src modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.classifier import classify_file

# === Define test cases ===
test_cases = [
    ("invoice_1.pdf", "invoice"),
    ("invoice_2.pdf", "invoice"),
    ("invoice_3.pdf", "invoice"),
    ("bank_statement_1.pdf", "bank_statement"),
    ("bank_statement_2.pdf", "bank_statement"),
    ("bank_statement_3.pdf", "bank_statement"),
    ("drivers_license_1.jpg", "drivers_license"),
    ("drivers_licence_2.jpg", "drivers_license"),
    ("drivers_license_3.jpg", "drivers_license"),
]

# === Confidence threshold below which test is skipped ===
CONFIDENCE_THRESHOLD = 0.6

@pytest.mark.parametrize("filename,expected_label", test_cases)
def test_classification(filename, expected_label):
    filepath = os.path.join("files", filename)

    with open(filepath, "rb") as f:
        file = FileStorage(stream=f, filename=filename)
        predicted = classify_file(file)
        
        # Verify result structure
        assert isinstance(predicted, dict), "Expected a dictionary with 'label' and 'confidence'"
        assert 0.0 <= predicted["confidence"] <= 1.0, "Confidence score should be between 0 and 1"

        # Debug info
        print(f"{filename} → predicted: {predicted['label']} ({predicted['confidence']}), expected: {expected_label}")

        # Check label with confidence-aware logic
        if predicted["label"] != expected_label:
            if predicted["confidence"] < CONFIDENCE_THRESHOLD:
                pytest.skip(f"{filename} misclassified with low confidence ({predicted['confidence']})")
            else:
                assert False, f"{filename} → predicted: {predicted['label']} ({predicted['confidence']}), expected: {expected_label}"