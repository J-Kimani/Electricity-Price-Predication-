import numpy as np
import json
import pickle
import streamlit as st
import base64
import pandas as pd

# load saved model
def load_saved_artifacts():
    global __data_columns
    global __model

    with open("./columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
    
    with open("./elect.pickle", "rb") as f:
        __model = pickle.load(f)



def predict_electricity(day, month, forcastwind, SLEA, SMPEA, temp, wind, co2, actualwind, load):
    # create a dictionary with the input data
    data = {
        'Day': [day],
        'Month': [month],
        'ForecastWindProduction': [forcastwind],
        'SystemLoadEA': [SLEA],
        'SMPEA': [SMPEA],
        'ORKTemperature': [temp],
        'ORKWindspeed': [wind],
        'CO2Intensity': [co2],
        'ActualWindProduction': [actualwind],
        'SystemLoadEP2': [load]
    }
    # create a dataframe from the input data and replace empty strings with NaN values
    df = pd.DataFrame(data).replace('', np.nan)
    # drop any rows with NaN values
    df.dropna(inplace=True)
    # convert dataframe to float type
    df = df.astype(float)
    # make prediction using the trained model
    prediction = np.round(__model.predict(df)[0])
    # return the predicted electricity price
    return prediction

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("11.jpg")

page_bg_img = f""" 
<style>
[data-testid="stAppViewContainer"]> .main {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid= "stHeader"]{{
background: rgba(0,0,0,0);
}}

</style>
"""

def main():
    # background image
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Title
    st.title('Electricity Price Prediction')

    # user instructions
    instructions = '<p style="font-family:Courier; color:White; font-size: 20px;">Worry no more about unexpectedly high electricity bills. Predict it before they hit you with the bill!!</p>'
    st.markdown(instructions, unsafe_allow_html=True)

    # user input
    day_of_week = st.selectbox("Select day of the week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    month = st.selectbox("Select month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    forcastwind = st.text_input("Wind Forecast")
    SLEA = st.text_input("System Load Forecast")
    SMPEA = st.text_input("Price Forecast")
    temp = st.text_input("Actual Temperature")
    wind = st.text_input("Wind Measured")
    co2 = st.text_input("Co2 Intensity")
    actualwind = st.text_input("Actual Wind")
    load = st.text_input("System Load")

    # convert day of the week to a number
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day_of_week)

    # convert month to a number
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"].index(month) + 1

    # prediction code
    bill = ''

    # prediction button
    if st.button('BILL'):
        bill = predict_electricity(day, month, forcastwind, SLEA, SMPEA, temp, wind, co2, actualwind, load)

    st.success(bill)

    # conclusions
    conclusion = '<p style="font-family:Courier; color:White; font-size: 20px;">PREDICTED BILLS MIGHT DEVIATE FROM THE ACTUAL BILL. BUT THIS MODEL IS TRUSTED TO PREDICT BILLS WITH HIGH ACCURACY</p>'

    st.markdown(conclusion, unsafe_allow_html=True)


if __name__ == '__main__':
    load_saved_artifacts()
    main()
