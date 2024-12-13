from ultralytics import YOLO

def train_model():
    model = YOLO("yolov8n.pt") 
    
    model.train(
        data="data/bccd_dataset/bccd.yaml",  
        epochs=50,                           
        imgsz=640,                           
        batch=16,                            
        project="runs/detect",               
        name="train",                        
        workers=4                            
    )

if __name__ == "__main__":
    train_model()

