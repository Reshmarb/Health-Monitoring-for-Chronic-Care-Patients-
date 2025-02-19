import streamlit as st
import pandas as pd
import joblib
import sqlite3
from datetime import datetime

# Load trained model
rf_model = joblib.load("diabetes_model.pkl")

# Create database if not exists
def create_db():
    with sqlite3.connect("clinic_data.db") as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS patients 
                     (Pregnancies INT, Glucose INT, BloodPressure INT, SkinThickness INT, 
                      Insulin INT, BMI REAL, DiabetesPedigreeFunction REAL, Age INT, Outcome INT, 
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
create_db()

# Customizing Streamlit UI
st.set_page_config(page_title="Diabetes Risk Predictor", page_icon="🩺", layout="centered")
st.markdown(
    """
    <style>
        div.stButton > button {
            width: 100%;
            background-color: #FF4B4B; /* Default Red */
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px;
        }
        div.stButton > button:hover {
            background-color: #FF6B6B;
        }
        div.stButton > button:nth-of-type(1) {
            background-color: #4CAF50 !important; /* Green for first button */
        }
        div.stButton > button:nth-of-type(1):hover {
            background-color: #45A049 !important;
        }
    </style>
    """,
    unsafe_allow_html=True)

# Title & Description
st.title("🩺 Diabetes Risk Prediction System")
st.write("### Enter patient details below to assess the risk of diabetes.")

# Input layout
col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input("🤰 Pregnancies", min_value=0, max_value=20, step=1)
    glucose = st.number_input("🩸 Glucose Level", min_value=0, max_value=300, step=1)
    blood_pressure = st.number_input("❤️ Blood Pressure", min_value=0, max_value=200, step=1)
    skin_thickness = st.number_input("📏 Skin Thickness", min_value=0, max_value=100, step=1)
with col2:
    insulin = st.number_input("💉 Insulin Level", min_value=0, max_value=500, step=1)
    bmi = st.number_input("⚖️ BMI", min_value=0.0, max_value=60.0, step=0.1)
    dpf = st.number_input("📊 Diabetes Pedigree Function", min_value=0.0, max_value=3.0, step=0.01)
    age = st.number_input("🎂 Age", min_value=1, max_value=120, step=1)

st.markdown("---")  # Separator line

# Predict button
if st.button("🚀 Predict Diabetes Risk"):
    # Prepare input data
    input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]],
                              columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                                       "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"])
    # Predict
    prediction = rf_model.predict(input_data)[0]
    
    # Store in database
    with sqlite3.connect("clinic_data.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO patients (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                  (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age, prediction))
        conn.commit()
    
    # Display results
    if prediction == 1:
        st.error("⚠️ High Risk of Diabetes! Consult a doctor immediately.")
    else:
        st.success("✅ No significant risk detected. Maintain a healthy lifestyle!")

# View stored data button
if st.button("📊 View Stored Data"):
    with sqlite3.connect("clinic_data.db") as conn:
        df = pd.read_sql_query("SELECT * FROM patients", conn)
        st.dataframe(df)
