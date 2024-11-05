import torch
import cv2
import pandas as pd

# Load the YOLOv5 model (you can choose 'yolov5s', 'yolov5m', 'yolov5l', or 'yolov5x' based on speed vs. accuracy)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Use 'yolov5s' for a smaller, faster model

# Initialize webcam video stream
cap = cv2.VideoCapture(0)  # Change to '0' for default camera, or specify a file path for a video file

while cap.isOpened():
    ret, frame = cap.read()  # Capture frame-by-frame
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLOv5 on the frame
    results = model(frame)

    # Draw the results on the frame
    results.render()  # Draw bounding boxes and labels on the frame

    # Display the frame with detected objects
    cv2.imshow('YOLOv5 Real-Time Object Detection', results.imgs[0])

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
