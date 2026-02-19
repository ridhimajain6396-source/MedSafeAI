from ocr.logic.symptom import get_symptom_advice
from database.med_db import medicine_db
from ocr.ocr_utils import extract_text
from ocr.logic.risk_engine import get_risk_output

import streamlit as st
import pytesseract
from PIL import Image

# Tesseract Path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------------- UI HEADER ----------------
st.title("MedSafe AI 💊")
st.write("AI-powered medical safety assistant")

# =====================================================
# ✅ MEDICINE CHECKER
# =====================================================

st.subheader("🔎 Medicine Safety Checker")

medicine = st.text_input("Enter medicine name")

if st.button("Check"):

    if medicine.strip() == "":
        st.error("Please enter a medicine name.")
    else:
        med = medicine.lower()

        if med in medicine_db:

            result = medicine_db[med]
            info = result["info"]
            risk = result["risk"]

            st.success(f"{medicine} found in database.")
            st.info(info)

            # use risk engine module
            status, message = get_risk_output(risk)

            if status == "success":
                st.success(message)
            elif status == "warning":
                st.warning(message)
            else:
                st.error(message)

        else:
            st.warning("Medicine not found in database.")

    st.write("⚠ Always consult a doctor for professional medical advice.")

# =====================================================
# ✅ OCR PRESCRIPTION SECTION
# =====================================================

st.divider()
st.subheader("📄 Prescription OCR")

uploaded_file = st.file_uploader(
    "Upload prescription image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Prescription", width=400)

    # ✅ use OCR utility module
    extracted_text = extract_text(image)

    st.write("### Extracted Text")
    st.write(extracted_text)

    # -------- AUTO MEDICINE DETECTION --------
    detected_medicine = None

    for med in medicine_db.keys():
        if med in extracted_text.lower():
            detected_medicine = med
            break

    if detected_medicine:

        info = medicine_db[detected_medicine]["info"]
        risk = medicine_db[detected_medicine]["risk"]

        st.success(f"Detected Medicine: {detected_medicine}")
        st.info(info)

        status, message = get_risk_output(risk)

        if status == "success":
            st.success(message)
        elif status == "warning":
            st.warning(message)
        else:
            st.error(message)

    else:
        st.warning("No known medicine detected.")

    st.write("⚠ OCR results may not always be perfect.")
    st.divider()
st.subheader("🩺 Symptom Checker")

symptom = st.text_input("Enter your symptom")

if st.button("Check Symptom"):
    advice = get_symptom_advice(symptom)
    st.info(advice)