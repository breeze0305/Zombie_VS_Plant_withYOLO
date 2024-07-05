
# Zombie VS Plant with YOLOv10

> [!IMPORTANT]  
> **This project does not provide game files or any other infringing materials. Users should find relevant files online. This project is for learning purposes only. Thank you.**

This project uses the `yolo v10n`, `opencv`, `pyautogui`, and `pygetwindow` Python libraries to automate the game "Zombie VS Plant."

This GitHub repository provides:
* Training methods
* Application execution code
* YOLO v10 pre-trained weights

## Demo
> The level is located in the adventure mode 2-5 of the first generation of the PC version of ZVP, or you can find the "Bowling Zombies" level in the "Mini-Games" section after completing the game. The adventure mode level is relatively simple. If your trained model cannot pass the "Bowling Zombies" level in the "Mini-Games" section, please try testing it in the adventure mode.

video:  
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/9QPceNWJzYY/0.jpg)](https://youtu.be/9QPceNWJzYY)

## Installation
### Setup
**Step 0.** It is recommended to use conda as a virtual environment management tool and use Python version 3.8 or higher.  
```bash
conda create -n zvp python=3.8
conda activate zvp
```

**Step 1.** Install requirements.txt
```bash
pip install -r requirements.txt
```

**Step 2.** Install torch
```bash
pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113

# Modify to a compatible torch version if needed
# https://pytorch.org/
```

**Step 3.** Check if GPU is detected
```python
import torch 
print(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

# If 'cuda' is displayed, the GPU is detected
```

## Training
This project is trained based on yolo v10n. Users can modify the training model to other compatible versions (e.g., yolov8).  
The reason for using yolo v10n is its faster speed, which is essential for this level due to high inference speed requirements.

### Preparing Dataset
The format of the files should follow the path format given by yolo's official guidelines, and they should be placed in the same root directory as the training code for ease of use.

```python
# Folder structure
├── zvp_yolov10
│   ├── dataset
│   │   ├── images
│   │   │   ├── 00001.jpg
│   │   │   ├── 00002.jpg
│   │   │   ├── ...
│   │   ├── labels
│   │   │   ├── 00001.txt
│   │   │   ├── 00002.txt
│   │   │   ├── ...
│   ├── yolo_train.py
│   ├── data.yaml
```
* 1. Modify the corresponding path in `data.yaml`
* 2. Modify parameters in `yolo_train.py`
* 3. Run `yolo_train.py` until the model stops training

> [!TIP]  
> **You can use tools like roboflow or labelimg to label the dataset and convert it to yolo format. (For relatively small datasets, it is recommended to use roboflow to label files)**

## Inference
> [!IMPORTANT]  
> **It is recommended to open the game and enter it before starting the program, and keep the game window at the front.**  
> **Use windowed mode. If you have multiple screens, ensure the game window remains on screen 1 so that `pyautogui` and `pygetwindow` can detect it correctly.**

### Weights
You can modify the weight path in `yolo_inference.py` to use your trained weights or use the pre-trained `best.pt`.
```bash
python yolo_inference.py
```

## Acknowledgement
* [yolov10](https://docs.ultralytics.com/models/yolov10/)
* [roboflow](https://app.roboflow.com/)
* [labelimg](https://github.com/HumanSignal/labelImg)
* [zombie vs plant](https://ggheart999.blogspot.com/2018/08/megapcslgplants-vs-zombies.html)
