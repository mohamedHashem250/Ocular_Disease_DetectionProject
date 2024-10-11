
import streamlit as st
import tensorflow as tf
from PIL import Image
from Classifier import Ocular_Disease_Detection_FromScratchModel



st.title("Deep Learning Classifier")
uploaded_file = st.file_uploader("Choose an image", type="jpg")
st.header("Ocular_Disease_Detection")
st.text("Upload a Image for to diagnose Ocular Disease")
if uploaded_file is not None:
	image = Image.open(uploaded_file)
	st.image(image, caption='Uploaded Image', use_column_width=True)
	st.write("Classifying...")
	#label,max_Prob  = Ocular_Disease_Detection_FromScratchModel(image, 'model_1_CNN.keras')
	label = Ocular_Disease_Detection_FromScratchModel(image, 'model_1_CNN.keras')
	st.write(f"Prediction: {label}, with Probability:{max_Prob }")
	if label == 'ACRIMA':
		    st.write("The illness is  ACRIMA")
	elif label ==  'Glaucoma':
		    st.write("The illness is  Glaucoma")
	elif label ==  'ODIR-5K':
		    st.write("The illness is  ODIR-5K")
	elif label == 'ORIGA':
		    st.write("The illness is  ORIGA")
	elif label == 'cataract':
		    st.write("The illness is  cataract")
	else:
		    st.write("The illness is  retina_disease")
