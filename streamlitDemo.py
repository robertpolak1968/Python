
#localhost:8501
#https://towardsdatascience.com/how-to-write-web-apps-using-simple-python-for-data-scientists-a227a1a01582
import streamlit as st
#x = st.slider('x')
#st.write(x, 'squared is', x * x)



import pandas as pd
import numpy as np
df = pd.read_csv("football_data.csv")
if st.checkbox('Show dataframe'):
    st.write(df)