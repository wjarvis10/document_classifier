import joblib
import os
import sys
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.text_extract import extract_text

# === Configuration ===
# Map label keywords to category names
#  - change based upon industry / file categories
CATEGORY_RULES = {
    "bank": "bank_statement",
    "invoice": "invoice",
    "licen": "drivers_license",
}

FILES_DIR = "../files"
OUTPUT_PATH = "../model/real_labeled_data.pkl"

# === Scalable collection ===
real_data = defaultdict(list)

for fname in os.listdir(FILES_DIR):
    fname_lower = fname.lower()
    label = None

    for keyword, category in CATEGORY_RULES.items():
        if keyword in fname_lower:
            label = category
            break

    if not label:
        continue  # skip unclassified files

    fpath = os.path.join(FILES_DIR, fname)
    ext = fname.rsplit(".", 1)[-1].lower()

    with open(fpath, "rb") as f:
        text = extract_text(f, ext)
        if text.strip():
            real_data[label].append(text)

# Save
joblib.dump(dict(real_data), OUTPUT_PATH)
print(f"✅ Saved {sum(len(v) for v in real_data.values())} documents to {OUTPUT_PATH}")