import torch
import pygetwindow
import pyautogui
import cv2
import numpy as np
from ultralytics import YOLO
from PIL.Image import Image

def take_shot(window:str)->Image:
    if window:
        x, y, width, height = window.left, window.top, window.width, window.height
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        
        return screenshot

def main():
    model = YOLO("best.pt") # yolo v10n.pt
    window_title = "眵昜湮桵蔗坌笢恅唳" # get zvp windows
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    while True:
        window = pygetwindow.getWindowsWithTitle(window_title)[0]

        screenshot = take_shot(window)

        screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR) #Image -> np.array; RGB -> BGR
        original_height, original_width = screenshot_np.shape[:2] # Get the height and width of the screenshot: zvp 640 x 720
        screenshot_resize = cv2.resize(screenshot_np, (640, 640)) # normalize the image to 640 x 640 for yolo model
        
        result = model.predict(source=screenshot_resize, imgsz=640, save=False)
        boxes = result[0].boxes.xyxy  # use absolute coordinates for 640 x 640
        
        for box in boxes:
            x1, y1, x2, y2 = box[:4]
            # transfer absolute coordinates for 640 x 640 -> 640 x720
            x1 = int(x1 * original_width / 640)
            y1 = int(y1 * original_height / 640)
            x2 = int(x2 * original_width / 640)
            y2 = int(y2 * original_height / 640)
            cv2.rectangle(screenshot_np, (x1, y1), (x2, y2), (0, 255, 0), 2) # draw boxes
            cv2.circle(screenshot_np, (int((x1 + x2) / 2), int((y1 + y2) / 2)), 1, (0, 0, 255), -1) # draw hit point
            pyautogui.click(x=window.left+(x1 + x2) / 2 , y=window.top+(y1 + y2) / 2, clicks=3) # hit three time for iron bucket zombie
        cv2.imshow("frame", screenshot_np)
        
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
