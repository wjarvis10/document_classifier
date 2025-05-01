from werkzeug.datastructures import FileStorage
from src.text_extract import extract_text
import joblib
import os

# === Load the trained supervised classifier ===
model_path = "model/supervised_classifier.pkl"

if os.path.exists(model_path):
    classifier_model = joblib.load(model_path)
    print("✅ Supervised classifier loaded.")
else:
    classifier_model = None
    print("❌ Classifier model not found. Run train_supervised.py first.")

def classify_file(file: FileStorage):
    """
    Classify a file based on extracted text using the trained supervised classifier.
    """
    
    filename = file.filename.lower()
    file_extension = filename.rsplit('.', 1)[-1].lower()

    # Extract text
    text = extract_text(file, file_extension).strip()
    if not text:
        return "error: unreadable or empty file"

    if classifier_model is None:
        return "error: classifier not initialized"

   # Get class probabilities
    probs = classifier_model.predict_proba([text])[0]
    predicted_index = probs.argmax()
    predicted_label = classifier_model.classes_[predicted_index]
    confidence = round(probs[predicted_index], 3)

    return {
        "label": predicted_label,
        "confidence": confidence
    }
