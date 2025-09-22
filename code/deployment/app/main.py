# streamlit_app.py
import streamlit as st
import requests
import os
# FastAPI endpoint (container name 'fastapi' when using Docker Compose)
FASTAPI_URL = os.getenv("FASTAPI_URL", "http://fastapi:8000/predict")# FASTAPI_URL = "http://127.0.0.1:8000/predict"


st.title("🚢 Titanic Survival Prediction")

st.write("Enter passenger details to predict survival:")

# Input fields for Titanic features
pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100, value=25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)
parch = st.number_input("Number of Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0)
embarked = st.selectbox("Port of Embarkation (Embarked)", ["C", "Q", "S"])

if st.button("Predict Survival"):
    input_data = {
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked
    }

    response = requests.post(FASTAPI_URL, json=input_data)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        if prediction == 1:
            st.success("✅ The passenger is predicted to **Survive**")
        else:
            st.error("❌ The passenger is predicted to **Not Survive**")
    else:
        st.error("Error: Could not get a prediction from the API")
