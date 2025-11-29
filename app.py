import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details below to predict heart disease.")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 1, 120, 45)
    sex = st.selectbox("Sex (1 = Male, 0 = Female)", [1, 0])
    cp = st.selectbox("Chest pain type (0-3)", [0, 1, 2, 3])
    bp = st.number_input("Resting BP", 80, 200, 120)

with col2:
    chol = st.number_input("Cholesterol", 100, 600, 200)
    ekg = st.selectbox("EKG results (0-2)", [0, 1, 2])
    maxhr = st.number_input("Max Heart Rate", 60, 220, 150)
    exang = st.selectbox("Exercise Angina (1 = Yes, 0 = No)", [1, 0])

with col3:
    st_depression = st.number_input("ST Depression", 0.0, 10.0, 1.0)
    slope = st.selectbox("Slope of ST (0-2)", [0, 1, 2])
    vessels = st.selectbox("Number of vessels fluro (0-3)", [0, 1, 2, 3])
    thallium = st.selectbox("Thallium (1 = Normal, 2 = Fixed, 3 = Reversible)", [1, 2, 3])

if st.button("Predict"):
    # Correct 12-feature input array
    features = np.array([[
        age,
        sex,
        cp,
        bp,
        chol,
        ekg,
        maxhr,
        exang,
        st_depression,
        slope,
        vessels,
        thallium
    ]])

    result = model.predict(features)[0]

    if result == 1:
        st.error("⚠️ High chance of Heart Disease")
    else:
        st.success("✅ No Heart Disease Detected")