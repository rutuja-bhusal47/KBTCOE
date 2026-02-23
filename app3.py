import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("Enter first number", step=1, format="%d")
num2 = st.number_input("Enter second number", step=1, format="%d")

operation=st.selectbox("choose Operation",["Addition","Subtraction","Multiplication","Division"])

if st.button("Calculate"):
    if operation=="Addition":
        st.write(num1+num2)

    elif operation=="Subtraction":
        st.write(num1-num2)

    elif operation=="Multiplication":
        st.write(num1*num2)

    elif operation=="Division":
        if num2!=0:
            st.write(num1/num2)
        else:
            st.write("Cannot divide by zero")