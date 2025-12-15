# Import required libraries: Streamlit for UI, pandas for data handling, joblib for loading models
import streamlit as st
import pandas as pd
import joblib

# Loading our model through Joblib
model = joblib.load("models/credit_model.pkl")

# Loading our encoders into a dictionary 
encoders = {col: joblib.load(f"models/{col}_encoder.pkl") for col in ["Sex", "Housing", "Saving accounts", "Checking account"]}

# Load target encoder
target_encoder = joblib.load("models/target_encoder.pkl")

st.title("Credit Risk Prediction App")
st.write("Enter applicant information to predict is the credit is risk or bad")

# Streamlit input widgets to collect user information for credit risk prediction
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", ["own", "rent", "free"])
saving_accounts = st.selectbox("Saving accounts", ["little", "moderate", "rich", "quite rich"])
checking_account = st.selectbox("Checking account", ["little", "moderate", "rich"])
credit_amount = st.number_input("Credit Amount", min_value=0, value=1000)
duration = st.number_input("Duration (Months)", min_value=1, value=12)

# Create a single-row DataFrame from user inputs (with categorical values encoded) for model prediction
df_input = pd.DataFrame({
    "Age": [age],
    "Sex": (encoders["Sex"].transform([sex])[0]),
    "Job": [job],
    "Housing": (encoders["Housing"].transform([housing])[0]),
    "Saving accounts": (encoders["Saving accounts"].transform([saving_accounts])[0]),
    "Checking account": (encoders["Checking account"].transform([checking_account])[0]),
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

# When user clicks 'Predict Risk', make a prediction and display result as GOOD or BAD
if st.button("Predict Risk"):
    prediction = model.predict(df_input)[0]
    decoded_prediction = target_encoder.inverse_transform([prediction])[0]
    
    if decoded_prediction.lower() == "good":
        st.success(f"The predicted credit risk is: {decoded_prediction}")
    else:
        st.error(f"The predicted credit risk is: {decoded_prediction}")


