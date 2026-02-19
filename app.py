import streamlit as st

st.title("MedSafe AI 💊")
st.write("AI-powered medical safety assistant")

medicine = st.text_input("Enter medicine name")

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