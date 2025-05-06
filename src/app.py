from flask import Flask, request, jsonify
from flask_cors import CORS
from src.classifier import classify_file
import logging

app = Flask(__name__)
CORS(app, resources={r"/classify_file": {"origins": "http://localhost:5173"}})

# Global logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),     # Write to file
        logging.StreamHandler()                  # Optional: also log to console
    ]
)

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'docx', 'xlsx', 'xls'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/classify_file', methods=['POST'])
def classify_file_route():

    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    file_class = classify_file(file)
    return jsonify({"file_class": file_class}), 200

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)
