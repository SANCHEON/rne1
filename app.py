import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv("/content/drive/MyDrive/기숙사수용현황분석.csv")
st.dataframe(data)

st.write("Hello World")