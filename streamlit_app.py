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
R = color_list['result'][0][0]
G = color_list['result'][0][1]
B = color_list['result'][0][2]
c = '<p style="font-family:sans-serif; color:rgb(%d,%d,%d); font-size: 42px;">New image</p>'
st.title("This is my first app")
st.write("hellow word")
st.info("This is my first homework")
if st.button('change color'):
 st.markdown('<p style="font-family:sans-serif; color:rgb(1,2,3); font-size: 42px;">New image</p>',unsafe_allow_html=True)
