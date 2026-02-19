import streamlit as st
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("MedSafe AI 💊")
st.write("AI-powered medical safety assistant")

medicine = st.text_input("Enter medicine name")

# Fake medicine database
medicine_db = {
    "paracetamol": "Generally safe when taken in proper dosage.",
    "ibuprofen": "May cause stomach irritation if taken without food.",
    "aspirin": "Avoid if you have bleeding disorders."
}

if st.button("Check"):

    # Step 1: Validation
    if medicine.strip() == "":
        st.error("Please enter a medicine name.")

    else:
        med = medicine.lower()

        # Step 2: Database Lookup
        if med in medicine_db:
            result = medicine_db[med]

            # Step 3: Risk Output
            st.success(f"{medicine} is found in database.")
            st.info(result)

        else:
            st.warning("Medicine not found in database.")

        # Step 4: Disclaimer
        st.write("⚠ Always consult a doctor for professional medical advice.")
        # ---------------- OCR SECTION ----------------

st.divider()
st.subheader("📄 Prescription OCR")

uploaded_file = st.file_uploader(
    "Upload prescription image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Prescription", use_column_width=True)

    # Extract text using OCR
    extracted_text = pytesseract.image_to_string(image)

    st.write("### Extracted Text")
    st.write(extracted_text)

    st.write("⚠ OCR results may not always be perfect.")