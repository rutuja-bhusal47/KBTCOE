import streamlit as st

st.title("Simple Form")

name = st.text_input("Enter your name")
date = st.date_input("Enter your date of birth")
gender= st.selectbox("Select your gender",["Male","Female"])
if st.button("Submit"):
    st.write("Name: ", name)
    st.write("Date of Birth: ", date)
    st.write("Gender: ", gender)