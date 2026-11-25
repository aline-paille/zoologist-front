import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

HEADERS = {'accept': '*/*'}

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)

"""
## Please, input the characteristics of the penguin.
We need to know all the inputs required by our model to make a prediction.
"""

island_option = st.selectbox('Select an island:', ["Biscoe", "Dream", "Torgersen"])

bill_length = st.number_input('Insert a bill length (in mm)')

bill_depth = st.number_input('Insert a bill depth (in mm)')

flipper_length = st.number_input('Insert a flipper length (in mm)')

body_mass = st.number_input('Insert a body mass (in g)')

sex_option = st.selectbox('Select a sex:', ["Male", "Female"])


# dict of parameters
params = {
    "island": island_option,
    "bill_length_mm": bill_length,
    "bill_depth_mm": bill_depth,
    "flipper_length_mm": flipper_length,
    "body_mass_g": body_mass,
    "sex": sex_option,
}

# manage the click button action: get predition
if st.button('Get Prediction'):
    response = requests.get(
        url=st.secrets["URL"],
        headers=HEADERS,
        params=params
    )
    if response.status_code != 200:
        st.write('Something went wrong during request ', response.status_code, response.text)
    else:
        # prediction = json.loads(response.text)["prediction"]
        prediction = response.json()["prediction"]
        st.write(f'The current prediction is **{prediction}**.')
else:
    st.write("You haven't una a prediction yet...")
