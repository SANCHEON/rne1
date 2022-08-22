import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv("기숙사수용현황분석.csv")
num1 = len(data['학교'].unique())

num2 = len(data[data['설립구분'] != '사립']['학교'].unique())
num3 = num1 - num2

col1, col2, col3 = st.columns(3)
col1.metric("전국 대학 수", num1, "")
col2.metric("국공립", num2, f(round(num2 / num1 * 100)) + "%")
col3.metric("사립", num3, num3 / num1 * 100)

st.dataframe(data)

