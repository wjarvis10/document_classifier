# Use a lightweight Python image
FROM python:3.11-slim

# Install system dependencies including Tesseract OCR
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libglib2.0-0 \
    libgl1-mesa-glx \
    poppler-utils \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask/Gunicorn will run on
EXPOSE 8080

# Start the Flask app using Gunicorn
CMD ["gunicorn", "src.app:app", "--bind", "0.0.0.0:8080"]
