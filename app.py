import streamlit as st
import pandas as pd
import joblib


st.title("Machine Learning Project")
st.write("Chronic Kidney Disease (CKD) Prediction")

model = joblib.load('best_model.pkl')

st.header("Enter Patient Information")


age = st.number_input("Age", value=50)
gender = st.selectbox("Gender", ["male", "female"])
blood_pressure = st.number_input("Blood Pressure", value=120)
specific_gravity = st.number_input("Specific Gravity", value=1.020, step=0.005)
albumin = st.number_input("Albumin",  value=4)
sugar = st.number_input("Sugar",  value=4)
pus_cell = st.selectbox("Pus Cell", ["normal", "abnormal"])
pus_cell_clumps = st.selectbox("Pus Cell Clumps", ["absent", "present"])
bacteria = st.selectbox("Bacteria", ["absent", "present"])
blood_glucose_random = st.number_input("Blood Glucose Random", value=100.0, step=0.1)
blood_urea = st.number_input("Blood Urea", value=30.0, step=0.1)
serum_creatinine = st.number_input("Serum Creatinine", value=1.0, step=0.01)
sodium = st.number_input("Sodium", value=139.0, step=0.1)
potassium = st.number_input("Potassium", value=4.0, step=0.1)
hemoglobin = st.number_input("Hemoglobin", value=12.0, step=0.1)
packed_cell_volume = st.number_input("Packed Cell Volume", value=40.0, step=0.1)
white_blood_cell_count = st.number_input("White Blood Cell Count", value=7000)
red_blood_cell_count = st.number_input("Red Blood Cell Count", value=4.5, step=0.1)
hypertension = st.selectbox("Hypertension", ["no", "yes"])
diabetes_mellitus = st.selectbox("Diabetes Mellitus", ["no", "yes"])
coronary_artery_disease = st.selectbox("Coronary Artery Disease", ["no", "yes"])
appetite = st.selectbox("Appetite", ["good", "poor"])
anemia = st.selectbox("Anemia", ["no", "yes"])
pedal_edema = st.selectbox("Pedal Edema", ["no", "yes"])

if st.button("Predict CKD Risk"):
    # Encoding
    gender_encoded = 1 if gender == "male" else 0
    albumin_encoded = 1 if albumin == "abnormal" else 0
    sugar_encoded = 1 if sugar == "abnormal" else 0
    pus_cell_encoded = 1 if pus_cell == "abnormal" else 0
    pus_cell_clumps_encoded = 1 if pus_cell_clumps == "present" else 0
    bacteria_encoded = 1 if bacteria == "present" else 0
    hypertension_encoded = 1 if hypertension == "yes" else 0
    diabetes_mellitus_encoded = 1 if diabetes_mellitus == "yes" else 0
    coronary_artery_disease_encoded = 1 if coronary_artery_disease == "yes" else 0
    appetite_encoded = 1 if appetite == "poor" else 0
    anemia_encoded = 1 if anemia == "yes" else 0
    pedal_edema_encoded = 1 if pedal_edema == "yes" else 0

   
    input_data = [[
        age, gender_encoded, blood_pressure, specific_gravity,
        albumin_encoded, sugar_encoded, pus_cell_encoded, pus_cell_clumps_encoded,
        bacteria_encoded, blood_glucose_random, blood_urea, serum_creatinine,
        sodium, potassium, hemoglobin, packed_cell_volume,
        white_blood_cell_count, red_blood_cell_count,
        hypertension_encoded, diabetes_mellitus_encoded,
        coronary_artery_disease_encoded, appetite_encoded,
        anemia_encoded, pedal_edema_encoded
    ]]

   
    prediction = model.predict(input_data)[0]

    st.header("Prediction Result")
    if prediction == 1:
        st.error("The patient likely has CKD.")
    else:
        st.success("The patient is unlikely to have CKD.")
