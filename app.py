from flask import Flask, render_template, request, redirect, send_from_directory
from ultralytics import YOLO
import os
import uuid
import cv2
import subprocess

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["OUTPUT_FOLDER"] = "static/outputs"


# Load model once
model = YOLO("weights/best.pt")

def convert_to_h264(input_path, output_path):
    command = [
        'ffmpeg',
        '-i', input_path,
        '-vcodec', 'libx264',
        '-acodec', 'aac',
        '-strict', 'experimental',
        output_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error opening video file")
        return
    
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        results = model(frame)
        
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = box.conf.item()
                class_id = box.cls.item()
                class_name = model.names[class_id]
                
                # Draw bounding box with thicker border
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)  # Red box, thickness 3

                # Add larger label
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)  # Bigger font, white text
        out.write(frame)
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video = request.files["video"]
        if video:
            filename = str(uuid.uuid4()) + "_" + video.filename
            input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            output_path = os.path.join(app.config["OUTPUT_FOLDER"], "processed_" + filename)
            video.save(input_path)
            # Convert uploaded video to H.264 for browser preview
            converted_input_path = os.path.join(app.config["UPLOAD_FOLDER"], "converted_" + filename)
            convert_to_h264(input_path, converted_input_path)

            converted_static_path = os.path.join(app.config["OUTPUT_FOLDER"], "converted_" + filename)
            os.rename(converted_input_path, converted_static_path)

            process_video(converted_static_path, output_path)
            return render_template(
                "index.html",
                input_video=os.path.basename(converted_static_path),
                output_video=os.path.basename(output_path)
            )
    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename)

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("static/outputs", exist_ok=True)
    app.run(debug=True)
