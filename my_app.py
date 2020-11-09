import streamlit as st
import numpy as np
import pandas as pd
import time

st.write("# AI Art") 

st.write("### Content Image")
st.file_uploader('File uploader', key="c")

st.write("### Style Image")
st.file_uploader('File uploader', key="s")

if st.button("Magic"): 
  my_bar = st.progress(0)
  for percent_complete in range(100):
      time.sleep(0.1)
      my_bar.progress(percent_complete + 1)
      
  st.spinner()
  with st.spinner(text='In progress'):
    time.sleep(5)
  st.success('Done')

st.write("### Output")
