from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests

data = '{"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
response.json()

st.title("This is my first app")
st.write("hellow word")
st.info("This is my first homework")
if st.button('change color'):
  st.markdown('color change', color= '[49,47,49]')
else:
  st.markdown('changed', color= '[91,83,81]')
