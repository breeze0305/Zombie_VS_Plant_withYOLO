from ultralytics import YOLO


def main():
    # Load YOLOv10n model 
    model = YOLO('yolov10n.pt')

    # Train the model
    model.train(data="data.yaml", epochs=1200, batch=32,imgsz=640, device=0)
    # device = 0 for cuda gpu
    # when model get overfitting , the yolo model will automatically stop to avoid wasting time.
    # be care of the training pic is already resize for 640 * 640
    # you can delete the batch arg to set auto batch
    
if __name__ == "__main__":
    main()
    
    