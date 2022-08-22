import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv("기숙사수용현황분석.csv")

col1, col2, col3 = st.columns(3)
col1.metric("전국 대학 수", "70 °F", "1.2 °F")
col2.metric("국공립", "9 mph", "-8%")
col3.metric("사립", "86%", "4%")

st.dataframe(data)

