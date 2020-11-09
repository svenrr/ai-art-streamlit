import streamlit as st
import numpy as np
import pandas as pd

st.write("# AI Art") 

st.write("### Content Image")
st.file_uploader('File uploader')

st.write("### Style Image")
st.file_uploader('File uploader')

if st.button("Magic"): 
  st.progress(progress_variable_1_to_100)
  st.spinner()
  with st.spinner(text='In progress'):
  time.sleep(5)
  st.success('Done')

st.write("### Output")
