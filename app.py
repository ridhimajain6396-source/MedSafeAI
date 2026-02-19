from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from modules.fuzzy_matcher import find_medicine
from modules.interaction_checker import check_interactions
from modules.ai_engine import ask_llm
from modules.ocr_processor import extract_text

st.set_page_config(page_title="MedSafe AI", layout="wide")
st.title("🧠 MedSafe AI")

tab1, tab2, tab3, tab4 = st.tabs([
    "Medicine Interaction",
    "Prescription OCR",
    "Symptom Guidance",
    "Emergency Risk"
])

with tab1:
    st.header("Medicine Interaction Checker")

    meds = st.text_area("Enter medicines (comma separated)")

    if st.button("Check"):
        inputs = [m.strip() for m in meds.split(",")]
        found = []

        for i in inputs:
            m = find_medicine(i)
            if m:
                found.append(m)

        st.write("Detected Medicines:", found)

        warnings = check_interactions(found)

        if warnings:
            st.error("⚠ Interaction Found")
            for w in warnings:
                st.write(w)

            explanation = ask_llm(
                f"Explain simply: {warnings}"
            )
            st.info(explanation)
        else:
            st.success("No major interactions detected")

with tab2:
    st.header("Prescription OCR")
    img = st.file_uploader("Upload prescription", type=["png", "jpg", "jpeg"])

    if img is not None:
        st.image(img)

        text = extract_text(img)

        if text.startswith("OCR Error"):
            st.error(text)
        else:
            st.text_area("Extracted Text", text, height=200)

            summary = ask_llm(
                f"Extract medicine names from the following prescription text and return them clearly:\n{text}"
            )
            st.info(summary)


with tab3:
    st.header("Symptom Guidance")
    symptoms = st.text_area("Describe symptoms")

    if st.button("Analyze"):
        response = ask_llm(
            f"Provide safe health guidance (no diagnosis): {symptoms}"
        )
        st.write(response)



with tab4:
    st.header("Emergency Risk Predictor")
