


import streamlit as st

st.title("Calculate Sqaure!")

def sqaure(x):
    return x*x

num = st.number_input("Inserting a number")

if(st.button("Sqaure it")):
    result = sqaure(num)
    st.text(result)