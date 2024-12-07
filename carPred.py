import streamlit as st
import pandas as pd
import pickle

st.title("Car Resale Price Prediction")

# load the model from disk.
# with open('car_pred_model', 'rb') as f:
#     model = pickle.load(f)

cars_df = pd.read_csv("./cars24-car-price.csv")
st.dataframe(cars_df.head())

col1, col2 = st.columns(2)
# dropdown
fuel_type = col1.selectbox("Select the fuel type",
                           ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

engine = col1.slider("Set the Engine Power",
                     500, 5000, step=100)

transmission_type = col2.selectbox("Select the transmission type",
                                   ["Manual", "Automatic"])

seats = col2.selectbox("Enter the number of seats",
                       [4,5,7,9,11])