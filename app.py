import streamlit as st
import pickle
import numpy as np

# -------------------------------------------------
# Load the trained Gradient Boosting model
# -------------------------------------------------
with open("model_gb.pkl", "rb") as file:
    model_gb = pickle.load(file)

# -------------------------------------------------
# App Title and Description
# -------------------------------------------------
st.title("🚗 Car Price Prediction App")
st.markdown("### Predict car prices using the trained Gradient Boosting Model")

st.write("Enter the following car details to get an estimated price:")

# -------------------------------------------------
# Input fields for car features
# -------------------------------------------------
wheelbase = st.number_input("Wheelbase", min_value=80.0, max_value=120.0, value=98.0)
carlength = st.number_input("Car Length", min_value=140.0, max_value=210.0, value=170.0)
carwidth = st.number_input("Car Width", min_value=60.0, max_value=72.0, value=65.0)
carheight = st.number_input("Car Height", min_value=47.0, max_value=60.0, value=53.0)
curbweight = st.number_input("Curb Weight", min_value=1500, max_value=4200, value=2500)
enginesize = st.number_input("Engine Size", min_value=60, max_value=210, value=120)
boreratio = st.number_input("Bore Ratio", min_value=2.5, max_value=4.0, value=3.3)
stroke = st.number_input("Stroke", min_value=2.5, max_value=4.0, value=3.3)
compressionratio = st.number_input("Compression Ratio", min_value=7.0, max_value=24.0, value=9.0)
horsepower = st.number_input("Horsepower", min_value=40, max_value=200, value=100)

# -------------------------------------------------
# Convert inputs to numpy array (order must match training)
# -------------------------------------------------
input_data = np.array([[wheelbase, carlength, carwidth, carheight,
                        curbweight, enginesize, boreratio, stroke,
                        compressionratio, horsepower]])

# -------------------------------------------------
# Prediction
# -------------------------------------------------
if st.button("Predict Price 💰"):
    predicted_price = model_gb.predict(input_data)[0]
    st.success(f"### 💵 Predicted Car Price: ${predicted_price:,.2f}")
