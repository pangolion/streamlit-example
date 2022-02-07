from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
st.title("This is my first app")
st.write("hellow word")
st.info("This is my first homework")
var url = "http://colormind.io/api/";
var data = {
	model : "default",
	input : [[44,43,44],[90,83,82],"N","N","N"]
}

var http = new XMLHttpRequest();

http.onreadystatechange = function() {
	if(http.readyState == 4 && http.status == 200) {
		var palette = JSON.parse(http.responseText).result;
	}
}

http.open("POST", url, true);
http.send(JSON.stringify(data));
