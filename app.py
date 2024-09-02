import streamlit as st
import joblib

model=joblib.load("model.pkl")

labels = {'0': 'addiction', '1': 'anxiety', '2': 'craving','3':'depression','4':'headache','5':'nausea','6':'tolerance','7':'withdrawal,'}
st.title("Adversive drug reaction prediction")

user_input=st.text_area("enter your text here")

if st.button("predict"):
    predicted_label = model.predict([user_input])[0]
    predicted = labels[str(predicted_label)]
    st.info(f"{predicted} ")
