import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = f'P:\\SkillWallet-Project\\Tesseract-OCR\\tesseract.exe'

def extract_text(uploaded_file):
    try:
        image_bytes = uploaded_file.read()
        image_stream = io.BytesIO(image_bytes)
        img = Image.open(image_stream)
        img = img.convert("RGB")
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"OCR Error: {str(e)}"
