from werkzeug.datastructures import FileStorage
from src.text_extract import extract_text
import joblib
import os
import logging

# === Load the trained supervised classifier ===
model_path = "model/supervised_classifier.pkl"

try:
    classifier_model = joblib.load(model_path)
    logging.info(f"success: Loaded classifier from {model_path}")
except FileNotFoundError:
    classifier_model = None
    logging.error(f"error: Model not found at {model_path}. Did you run train_supervised.py?")
except Exception as e:
    classifier_model = None
    logging.exception(f"error: Unexpected error while loading model: {e}")

def classify_file(file: FileStorage):
    """
    Classify a file based on extracted text using the trained supervised classifier.
    """
    
    filename = file.filename.lower()
    file_extension = filename.rsplit('.', 1)[-1].lower()

    # Extract text
    text = extract_text(file, file_extension).strip()
    if not text:
        return "Error: unreadable or empty file"

    if classifier_model is None:
        return "Error: classifier not initialized"

   # Get class probabilities
    probs = classifier_model.predict_proba([text])[0]
    predicted_index = probs.argmax()
    predicted_label = classifier_model.classes_[predicted_index]
    confidence = round(probs[predicted_index], 3)

    return predicted_label, confidence
