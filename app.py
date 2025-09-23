import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import plotly.express as px


# Load trained Random Forest model
model_path = r"C:\Users\elroy\OneDrive\Desktop\mlproject\rf_model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Streamlit page setup
st.set_page_config(page_title="Energy Consumption Predictor", layout="wide")
st.title("🏠 Household Energy Consumption Predictor")
st.markdown(
    """
    Predict **household energy usage (Wh)** based on environmental and time features.
    Model predicts `log_energy`, output converted to **Wh** using `2 ** log_energy`.
    """
)

# Map display names to model features
feature_display = {
    'Outside Temperature (°C)': 'T_out',
    'Outside Pressure (mm Hg)': 'Press_mm_hg',
    'Outside Humidity (%)': 'RH_out',
    'Windspeed (m/s)': 'Windspeed',
    'Visibility (km)': 'Visibility',
    'Dew Point (°C)': 'Tdewpoint',
    'Day of Month': 'day_of_month',
    'Day of Week': 'day_of_week',
    'Month': 'month',
    'Hour of Day': 'hour',
    'Mean Indoor Temperature (°C)': 'T_mean',
    'Max Indoor Temperature (°C)': 'T_max',
    'Min Indoor Temperature (°C)': 'T_min',
    'Std Indoor Temperature': 'T_std',
    'Mean Indoor Humidity (%)': 'RH_mean',
    'Max Indoor Humidity (%)': 'RH_max',
    'Min Indoor Humidity (%)': 'RH_min',
    'Std Indoor Humidity': 'RH_std'
}

# Sidebar inputs
st.sidebar.header("Input Features")
user_input = {}
for display_name, col_name in feature_display.items():
    if "Day" in display_name or "Hour" in display_name or "Month" in display_name:
        user_input[col_name] = st.sidebar.number_input(display_name, min_value=0, step=1)
    else:
        user_input[col_name] = st.sidebar.number_input(display_name, value=0.0, step=0.01, format="%.3f")

# Convert to DataFrame
input_df = pd.DataFrame([user_input])

# Predict button
if st.button("Predict Energy"):
    # Single prediction
    log_energy_pred = float(model.predict(input_df)[0])
    energy_wh = 2 ** log_energy_pred
    st.success(f"Predicted Energy Consumption: **{energy_wh:.2f} Wh**")

    # Gauge chart
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=energy_wh,
        title={'text': "Predicted Energy (Wh)"},
        gauge={
            'axis': {'range': [0, max(energy_wh*1.5, 500)]},  # adjust max range dynamically
            'bar': {'color': "orange"},
            'steps': [
                {'range': [0, energy_wh*0.5], 'color': "lightgreen"},
                {'range': [energy_wh*0.5, energy_wh], 'color': "yellow"},
                {'range': [energy_wh, energy_wh*1.5], 'color': "red"}
            ],
        }
    ))
    st.plotly_chart(fig_gauge)

    # 24-hour trend
    hours = list(range(24))
    input_df_trend = pd.concat([input_df]*24, ignore_index=True)
    input_df_trend['hour'] = hours
    preds = [2 ** model.predict(input_df_trend.iloc[[i]])[0] for i in range(24)]

    import plotly.express as px

    fig2 = px.line(
        x=hours,
        y=preds,
        labels={'x':'Hour of Day', 'y':'Predicted Energy (Wh)'},
        title="Predicted Energy Trend Across a Day",
        markers=True
    )
    st.plotly_chart(fig2)

# Input ranges note
st.markdown("---")
st.markdown("**Note:** Inputs must match the scale used during model training.")
st.markdown(
    """
    | Feature                     | Min     | Max     |
    |-----------------------------|---------|---------|
    | Outside Temperature (°C)    | -4.9    | 19.33   |
    | Outside Pressure (mm Hg)    | 736.77  | 772.27  |
    | Outside Humidity (%)        | 40.83   | 100     |
    | Windspeed (m/s)             | 0       | 10.33   |
    | Visibility (km)             | 12.67   | 56.5    |
    | Dew Point (°C)              | -6.4    | 13.5    |
    | Day of Month                | 1       | 31      |
    | Day of Week                 | 0       | 6       |
    | Month                       | 1       | 5       |
    | Hour of Day                 | 0       | 23      |
    | Mean Indoor Temperature (°C)| 14.73   | 24.44   |
    | Max Indoor Temperature (°C) | 18.09   | 27.03   |
    | Min Indoor Temperature (°C) | -5.62   | 21.43   |
    | Std Indoor Temperature      | 0.93    | 8.43    |
    | Mean Indoor Humidity (%)    | 29.5    | 54.79   |
    | Max Indoor Humidity (%)     | 36.9    | 99.9    |
    | Min Indoor Humidity (%)     | 1       | 45.75   |
    | Std Indoor Humidity         | 1.95    | 20.78   |
    """
)
