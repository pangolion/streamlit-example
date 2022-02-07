from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests

data = '{"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
color_list = response.json()
st.write(color_list['result'][1][1])

c = '<p style="font-family:sans-serif; color:rgb(214,78,69); font-size: 42px;"> color</p>'
st.title("This is my first app")
st.write("hellow word")
st.info("This is my first homework")
if st.button('change color'):
  st.markdown(c, unsafe_allow_html=True)
