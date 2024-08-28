from ultralytics import YOLO

if __name__ == '__main__':
    
    model = YOLO('yolov8n.pt')  

    
    results = model.train(data="C:/.../", epochs=100, imgsz=640,
                          device="cuda")