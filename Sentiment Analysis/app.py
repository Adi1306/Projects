import streamlit as st 
import numpy as np 
import joblib
from PIL import Image
st.title("RESTAURANT REVIEWS ANALYSIS")
image = Image.open('/content/food.jpg')
st.image(image)
message_text = st.text_input("Enter a message for review analysis")
model = joblib.load('/content/Project')
result = model.predict([message_text])[0]
if st.button("Predict"): 
 if result == 0:
	  st.success('Negative Review')    
 else:
	   result == 1
	   st.success('Positive Review')       
