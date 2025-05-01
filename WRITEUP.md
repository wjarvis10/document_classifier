# Heron File Classifier

This project provides a production-ready pipeline for classifying financial documents (e.g., invoices, bank statements, and driver’s licenses) using text extraction and a supervised machine learning model.

It supports PDFs, images, Word documents, and Excel files and can be easily extended to other document types and industries.

---

## 🚀 Features

- Text extraction from `.pdf`, `.jpg`, `.png`, `.docx`, `.xlsx`, and `.xls` files
- OCR support using Tesseract for scanned documents
- Synthetic data generation to augment small real-world datasets
- Trainable classifier using TF-IDF and Logistic Regression
- REST API using Flask to classify files
- Automated testing with confidence-based thresholds
- Logging to file (`logs/app.log`) for observability

---

## 📦 Getting Started

### 1. Clone the repository

git clone <repository_url>
cd heron_classifier

### 2. Set Up the repository

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Install Tesseract OCR

Tesseract is required for OCR-based image classification.

macOS: brew install tesseract

## Pipeline Overview

### 1. Extract Text from Real Documents

python scripts/collect_labeled_text.py

This will extract and label documents in files/ and save them to model/real_labeled_data.pkl

### 2. Generate Synthetic Data

python scripts/generate_synthetic_data.py

This creates realistic fake documents per type and saves them to model/synthetic_data.pkl

- Can change the number of synthetic examples by changing SAMPLES_PER_TYPE in generate_synthetic_data.py

### 3. Train Supervised Classifier

python scripts/train_supervised_model.py

This loads real + synthetic data, trains a model, and saves it to model/supervised_classifier.pkl

### Run the API Server

python -m src.app

Available endpoints:

- POST /classify_file: Upload a file and receive { label, confidence }
- GET /health: Health check

### Run Test Suite

pytest tests/

Tests validate document classification with confidence-based logic. Failing tests show predictions and confidence levels.

### Example API Usage (with curl)

curl -X POST -F 'file=@files/invoice_1.pdf' http://127.0.0.1:5000/classify_file

Expected Response:

{
"file_class": {
"label": "invoice",
"confidence": 0.934
}
}

## Easily Extend To Other Industries

1. Update CATEGORY_RULES in collect_labeled_text.py
2. Add new synthetic generators in generate_synthetic_data.py
3. Retrain and redeploy

## Notes

For best performance, ensure your synthetic examples closely resemble the structure of real-world files.
