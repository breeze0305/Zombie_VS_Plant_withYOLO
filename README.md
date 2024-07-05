# Zombie VS Plant with YOLOv10

> [!IMPORTANT]  
> **在此專案中，並沒有提供遊戲檔案等其他侵權素材，請使用者自行在網路上尋找相關文件，此專案僅供學習使用，謝謝大家。**

此專案利用```yolo v10n```、```opencv```、```pyautogui```、```pygetwindow```這幾個python庫，來完成zvp的自動遊戲。

在此github中提供了
* 訓練的方法
* 應用執行的相關程式碼
* yolo v10訓練好的權重

## Installation
### setup
**Step 0.** 推薦使用conda作為虛擬環境管理工具，並且使用python3.8以上版本。  
```bash
conda create -n zvp python=3.8
conda activate zvp
```

**Step 1.** 安裝requirements.txt
```bash
pip install -r requirements.txt
```

**Step 2.** 安裝torch
```bash
pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113

# 可自行修改至兼容的torch版本
# https://pytorch.org/
```

**Step 3.** 確認GPU是否偵測到
```python
import torch 
print(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

# 顯示cuda代表有偵測到gpu
```

## Training
本專案是基於yolo v10n進行訓練，使用者可以自行修改訓練模型至其他兼容版本。(如yolov8)  
使用yolo v10n的原因是因為其速度較快，在此關卡中對推理速度要求較高。  

### Preparing Dataset
文件的格式請依照yolo官方給定的路徑格式，並且將其放置在與訓練程式碼同一個根目錄下，方便使用。

```python
# 資料夾結構
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
* 1.修改對應的path路徑 ```data.yaml```
* 2.修改```yolo_train.py```中的參數
* 3.執行```yolo_train.py```直到模型停止訓練

> [!TIP]  
> **可以使用roboflow或者labelimg等工具來標記資料集，並且轉換成yolo格式。(資料集相對較小時，推薦使用roboflow來標記檔案)**



## Inference
> [!IMPORTANT]  
> **建議在啟動程式前，優先將遊戲打開進入遊戲，並且將遊戲視窗放在最前面。**
> **請使用窗口化，如果有多個螢幕，請確保遊戲視窗保持在 【螢幕1】 上以便```pyautogui```和```pygetwindow```可以正確的偵測到。**

### weights
可自行在```yolo_inference.py```中修改自行訓練的權重路徑，或者使用我訓練好的```best.pt```。
```bash
python yolo_inference.py
```


## Acknowledgement
* [yolov10](https://docs.ultralytics.com/models/yolov10/)
* [robosflow](https://app.roboflow.com/)
* [labelimg](https://github.com/HumanSignal/labelImg)
* [zombie vs plant](https://ggheart999.blogspot.com/2018/08/megapcslgplants-vs-zombies.html)