import streamlit as st 
import pandas as pd

st.title("Olympics Data Analysis")
st.sidebar.radio(
    'Select an option',
    (
    'Medal Tally', 
    'Overall Analysis', 
    'Country-wise Analysis', 
    'Athelete wise Analysis'
    )
)
