from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
st.title("This is my first app")
st.write("hellow word")
st.info("This is my first homework")

data = '{"model":"default"}'
response = requests.post('http://colormind.io/api/', data=data)
response.json()

print(data)
