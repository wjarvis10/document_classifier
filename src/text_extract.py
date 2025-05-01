import fitz  # PyMuPDF (used as fallback)
import pdfplumber
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from docx import Document
import pandas as pd
import tempfile
import logging

def extract_text(file, filetype):
    
    if filetype == "pdf":
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(file.read())
                tmp.flush()
                with pdfplumber.open(tmp.name) as pdf:
                    text = "\n".join([page.extract_text() or "" for page in pdf.pages])
            return text.strip()
        except Exception as e:
            logging.warning(f"[fallback] pdfplumber failed: {e}, using PyMuPDF")
            file.seek(0)
            text = ""
            with fitz.open(stream=file.read(), filetype="pdf") as doc:
                for page in doc:
                    text += page.get_text()
            return text.strip()
    
    elif filetype in ["png", "jpg", "jpeg"]:
        try:
            image = Image.open(file)
            # Preprocess: grayscale, contrast, sharpen
            image = image.convert("L")
            image = ImageEnhance.Contrast(image).enhance(2)
            image = image.filter(ImageFilter.SHARPEN)
            return pytesseract.image_to_string(image).strip()
        except Exception as e:
            logging.error(f"[error] image OCR failed: {e}")
            return ""

    elif filetype == "docx":
        document = Document(file)
        return "\n".join([para.text for para in document.paragraphs])

    elif filetype in ["xlsx", "xls"]:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
                tmp.write(file.read())
                tmp.flush()
                df = pd.read_excel(tmp.name, dtype=str)
            return df.fillna("").astype(str).agg(" ".join, axis=1).str.cat(sep=" ").strip()
        except Exception as e:
            logging.error(f"[error] Excel read failed: {e}")
            return ""
    
    else: 
        return ""