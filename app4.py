import streamlit as st

st.title("Simple chatbot")

Question=st.text_input("Ask me Anything...")
if st.button("Send"):
    st.write("You said: ", Question)
    st.write("Chatbot is on the process i will reply soon")