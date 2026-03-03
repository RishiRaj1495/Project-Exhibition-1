import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# --- LOAD YOUR SAVED ARTIFACTS ---
xgb_model = joblib.load('xgb_model.pkl')
fnn_model = load_model('fnn_model.h5')
scaler = joblib.load('scaler.pkl')
model_columns = joblib.load('model_columns.pkl')

st.set_page_config(page_title="Electricity Bill Forecaster", page_icon="⚡")

# --- PAGE SETUP ---
st.title('⚡ Electricity Bill Forecaster')
st.write("""
This app predicts your monthly electricity bill using two advanced machine learning models. 
Provide your usage details in the sidebar to get a prediction.
""")

# --- USER INPUT SIDEBAR ---
st.sidebar.header('Enter Your Usage Details')

def get_user_input():
    city = st.sidebar.selectbox('City', ['Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Hyderabad', 'Bengaluru'])
    temp = st.sidebar.slider('Temperature (°C)', 10.0, 50.0, 28.0, 0.1)
    humidity = st.sidebar.slider('Humidity (%)', 10.0, 100.0, 65.0, 0.1)
    weather = st.sidebar.selectbox('Weather Condition', ['Clear', 'Cloudy', 'Hazy', 'Sunny'])
    appliance = st.sidebar.selectbox('Primary Appliance', ['Air Conditioner', 'Refrigerator', 'Fan', 'Geyser', 'Microwave Oven', 'Television'])
    time_used = st.sidebar.slider('Hours Used Per Day', 0.1, 24.0, 3.0, 0.1)
    consumption = st.sidebar.slider('Consumption (kWh)', 0.1, 10.0, 1.5, 0.1)
    tariff = st.sidebar.slider('Tariff (INR per kWh)', 4.0, 12.0, 7.5, 0.01)

    data = {
        'Temperature_C': temp,
        'Humidity_Percent': humidity,
        'Time_Used_Hours': time_used,
        'Consumption_kWh': consumption,
        'Tariff_Applied_INR_per_kWh': tariff,
        'City': city,
        'Weather_Condition': weather,
        'Appliance_Name': appliance
    }
    
    return pd.DataFrame(data, index=[0])

# Get user input and display it
input_df = get_user_input()
st.subheader('Your Input:')
st.dataframe(input_df)

# --- PREDICTION LOGIC ---
if st.button('Forecast My Bill!'):
    processed_df = input_df.copy()
    processed_df = pd.get_dummies(processed_df, columns=['City', 'Weather_Condition', 'Appliance_Name'])
    
    for col in model_columns:
        if col not in processed_df.columns:
            processed_df[col] = 0
    
    final_input = processed_df[model_columns]

    # --- Make Predictions ---
    xgb_prediction = xgb_model.predict(final_input)
    scaled_input = scaler.transform(final_input)
    fnn_prediction = fnn_model.predict(scaled_input)

    # --- NEW: Calculate the Average Prediction ---
    avg_prediction = (xgb_prediction[0] + fnn_prediction[0][0]) / 2

    # --- DISPLAY RESULTS ---
    st.subheader('📈 Prediction Results')
    
    # --- NEW: Display the Final Projected Bill ---
    st.success(f"Final Projected Bill (Average): ₹ {avg_prediction:.2f}")
    st.markdown("---") # Adds a horizontal line

    # Display the individual model predictions
    col1, col2 = st.columns(2)
    with col1:
        st.info("XGBoost Prediction")
        st.write(f"**₹ {xgb_prediction[0]:.2f}**")

    with col2:
        st.info("Neural Network (FNN) Prediction")
        st.write(f"**₹ {fnn_prediction[0][0]:.2f}**")