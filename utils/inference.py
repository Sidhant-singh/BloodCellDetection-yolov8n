from ultralytics import YOLO
from PIL import Image
import numpy as np

# Load the fine-tuned model
model = YOLO('model/yolov10.pt')

def detect_objects(image_path):
    image = Image.open(image_path)
    results = model.predict(source=np.array(image), imgsz=640)
    return results
