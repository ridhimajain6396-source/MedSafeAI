import streamlit as st
import pytesseract
from PIL import Image

# Tesseract Path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------------- UI HEADER ----------------
st.title("MedSafe AI 💊")
st.write("AI-powered medical safety assistant")

# ---------------- MEDICINE DATABASE ----------------
medicine_db = {
    "paracetamol": {
        "info": "Generally safe when taken in proper dosage.",
        "risk": "LOW"
    },
    "ibuprofen": {
        "info": "May cause stomach irritation if taken without food.",
        "risk": "MEDIUM"
    },
    "aspirin": {
        "info": "Avoid if you have bleeding disorders.",
        "risk": "HIGH"
    }
}

# =====================================================
# ✅ MANUAL MEDICINE CHECKER
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

            # Risk display
            if risk == "LOW":
                st.success("Risk Level: LOW ✅")
            elif risk == "MEDIUM":
                st.warning("Risk Level: MEDIUM ⚠")
            else:
                st.error("Risk Level: HIGH 🚨")

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

    # Show uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Prescription", width=400)

    # OCR Extraction
    extracted_text = pytesseract.image_to_string(image)

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

        if risk == "LOW":
            st.success("Risk Level: LOW ✅")
        elif risk == "MEDIUM":
            st.warning("Risk Level: MEDIUM ⚠")
        else:
            st.error("Risk Level: HIGH 🚨")

    else:
        st.warning("No known medicine detected.")

    st.write("⚠ OCR results may not always be perfect.")