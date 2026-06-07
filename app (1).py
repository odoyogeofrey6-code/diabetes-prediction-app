
import streamlit as st
import joblib

model = joblib.load("knn_model.pkl")

st.title("Diabetes Prediction System")

pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bloodpressure = st.number_input("Blood Pressure", min_value=0)
skinthickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1)

if st.button("Predict"):
    prediction = model.predict([[
        pregnancies,
        glucose,
        bloodpressure,
        skinthickness,
        insulin,
        bmi,
        dpf,
        age
    ]])

    if prediction[0] == 1:
        st.error("Diabetes Detected")
    else:
        st.success("No Diabetes Detected")
