# 🔥 Fire and Smoke Detection System 
A web-based application that automatically detects fire and smoke in uploaded video files using the YOLOv8 deep learning model. The system visually highlights hazardous areas and provides an annotated video output, improving emergency response times and safety monitoring.
## 📌 Features
> ✅ Detects both fire and smoke in real-time or recorded videos.

> 🎯 Uses YOLOv8, a state-of-the-art object detection model.

> 🎥 Supports video previews before and after detection.

> 🖼️ Draws clear, labeled bounding boxes over fire/smoke regions.

> 📦 Allows users to download the processed video.

> 💻 Provides a styled web interface with loading animation for better user experience.
## 🚀 Demo
 <p align="center"> <img src="demos/output_video2.mp4" alt="Demo GIF" width="80%"> </p>
 
 ---
 ## 🧠 Model Information
- ***Architecture:*** YOLOv8 (You Only Look Once, version 8)

- ***Capabilities:***

    - Detects multiple instances of fire and smoke

    - Outputs confidence scores for each detection

    - Runs with minimal latency for efficient processing
    
## 🏗️ System Architecture
1. ***Upload:*** User uploads a video via the web interface

2. ***Conversion:*** Video is converted to H.264 format using FFmpeg

3. ***Detection:*** Frame-by-frame analysis using YOLOv8

4. ***Annotation:*** Bounding boxes and labels drawn on detections

5. ***Output:*** Processed video is rendered for preview and download

## 📷 Image Processing Pipeline

- ***Frame Extraction:*** Each video frame is processed sequentially

- ***Detection:*** YOLOv8 detects fire and smoke regions

- ***Bounding Box Drawing:*** Clear rectangles and labels are drawn with confidence scores

- ***Rendering:*** Processed video is saved and presented via UI

## 🌐 Web UI Highlights
- Styled with vibrant, responsive design

- Video previews:

    - Before processing

    - After detection

- Progress bar with animated fire theme

- Intuitive download button
 
## 📁 Project Structure
```
project/
│
├── static/
│   └── outputs/           # Processed videos
├── templates/
│   └── index.html         # Main web UI
├── uploads/               # Uploaded videos
├── weights/
│   └── best.pt            # Trained YOLOv8 model
├── demos/                 # Some Demos Videos
├── requirements.txt       # requried packages
├── app.py                 # Flask application
└── README.md              # You are here!
```

## ⚙️ Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/Jawad-02/fire-smoke-detector.git
cd fire-smoke-detector
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Ensure FFmpeg is installed
```bash
# Ubuntu
sudo apt install ffmpeg

# Windows (Use installer or add ffmpeg to PATH)
```
4. Run the Flask app
```bash
python app.py
```
5. Open in browser
```
http://127.0.0.1:5000/
```
## 🔮 Future Enhancements

- 🔴 Live camera feed support for real-time detection

- 📢 Integration with alert/notification systems

- 📊 Dashboard for monitoring multiple video streams

- 🧊 Edge deployment on surveillance cameras

- 📐 Performance metrics tracking and evaluation

## 🧾 License
MIT License – free for personal and commercial use.

## 👨‍💻 Author

Developed by *Jawad-02* as part of a final year project in image processing and computer vision.
 