# import sys
# import os
# import joblib
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from src.text_extract import extract_text

# TEST_FOLDER = "../files"

# for fname in os.listdir(TEST_FOLDER):
#     if not fname.lower().endswith(('pdf', 'jpg', 'jpeg', 'png', 'docx', 'xlsx', 'xls')):
#         continue

#     fpath = os.path.join(TEST_FOLDER, fname)
#     ext = fname.rsplit('.', 1)[-1].lower()

#     print(f"\n🧪 Extracting from: {fname}")
#     with open(fpath, "rb") as f:
#         text = extract_text(f, ext)
#         print(text[:1000])  # print first 1000 characters to avoid overflow
#         print("\n" + "-" * 80)


# real_data = joblib.load("../model/real_labeled_data.pkl")
# for label, docs in real_data.items():
#     print(f"{label}: {len(docs)} documents")
#     # print(docs[0][:300])