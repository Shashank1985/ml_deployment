#deploying the symptom to disease model using streamlit
#done by Shashank1985 on 30/06/2023

import streamlit as st
import pandas as pd
import pickle
model= pickle.load(open("model.pkl",'rb'))
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
st.write("NLP models work best when you are as specific as possible with your input. Please note that AI models might not always give 100% accurate results and it is always better to consult with the doctor")
st.write("This model helps you gain a better understanding of what disease you might have")
x = st.text_input("enter symptoms")
x1 = [x]

if st.button('Predict disease: '):
    output = predict(x1)
    output = list_to_string(output)
    st.success("The predicted disease is: " + output)
