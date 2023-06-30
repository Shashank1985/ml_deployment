#deploying the symptom to disease model using streamlit
#done by Shashank1985 on 30/06/2023

import streamlit as st
import pandas as pd
import pickle
model= pickle.load(open("ml_deployment/model.pkl",'rb'))
def predict(text):
    prediction = model.predict(text)
    return prediction
def list_to_string(s):
    s = ""
    for ele in s:
        s += ele
    return s
st.title("""WELCOME""")
st.header("Enter your symptoms")

x = st.text_input("enter symptoms")
x1 = [x]

if st.button('Predict disease: '):
    output = predict(x1)
    st.success(output)
