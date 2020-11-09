import streamlit as st
import numpy as np
import pandas as pd
import time

st.write("# AI Art") 

st.write("In the following an attempt is made to generate a new image. For this purpose two images are necessary as starting point. A content image and a style image. The algorithm tries to apply or imitate the style of one image to the other image.")

st.write("placeholder for example")

st.write("### Content Image")
st.file_uploader('File uploader', key="c")

st.write("### Style Image")
st.file_uploader('File uploader', key="s")

if st.button("Generate new image"): 
  my_bar = st.progress(0)
  st.spinner()
  with st.spinner(text='In progress'):
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
  st.success('Done')

st.write("### Output")
