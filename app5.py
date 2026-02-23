import streamlit as st


st.markdown("""
<style>
            .stButton > button 
            {
                background-color: green;
                color: white;
                border-radius: 50%;
            }
</style>





""",unsafe_allow_html=True)








st.title("Welcome to basic streamlit app")

age= st.slider("Select your age",1,100)

city= st.selectbox("select your city",["Delhi","Mumbai","Pune","nashik"])
if st.button("Show details"):
    st.write("Age ", age)
    st.write("City ", city)