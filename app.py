import streamlit as st
from PIL import Image
from ultralytics import YOLO

model = YOLO("yolov8n.pt") 

st.title("Blood Cell Detection")
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    results = model(image)
    st.image(results[0].plot(), caption="Detected Blood Cells")
