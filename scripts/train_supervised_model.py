import joblib
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import logging

# === Load real and synthetic data ===
real_data = joblib.load("model/real_labeled_data.pkl")
synthetic_data = joblib.load("model/synthetic_data.pkl")

# === Combine and flatten ===
docs, labels = [], []

for label, texts in {**real_data, **synthetic_data}.items():
    for text in texts:
        docs.append(text)
        labels.append(label)

# === Train/test split for optional evaluation ===
X_train, X_test, y_train, y_test = train_test_split(
    docs, labels, test_size=0.2, random_state=42
)

# === Train classifier pipeline ===
pipeline = make_pipeline(
    TfidfVectorizer(stop_words="english"),
    LogisticRegression(max_iter=1000)
)

pipeline.fit(X_train, y_train)

# === Evaluate ===
y_pred = pipeline.predict(X_test)
logging.info("Success: Model trained. Classification report:")
logging.info(classification_report(y_test, y_pred))

# === Save classifier ===
joblib.dump(pipeline, "model/supervised_classifier.pkl")
logging.info("Success: Model saved to model/supervised_classifier.pkl")