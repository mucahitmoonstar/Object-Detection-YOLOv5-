
**ABOUT YOLO ALGORİTHM**

The YOLO (You Only Look Once) algorithm is a popular, efficient deep learning model used for real-time object detection in images and video streams. Unlike traditional object detection models that examine parts of the image multiple times, YOLO uses a single, unified model to predict object locations and labels in one pass. This design makes it exceptionally fast and suitable for applications requiring real-time detection, such as surveillance, autonomous driving, and robotics.

**How YOLO Works**
The core of YOLO is its unique approach to breaking down an image into a grid, then predicting bounding boxes and class probabilities for each grid cell. Here’s a simplified breakdown:

**Grid Division:**
YOLO divides the input image into an S×S grid (e.g., 7x7). Each grid cell is responsible for detecting objects whose center falls within that cell.

Bounding Boxes: For each grid cell, YOLO predicts multiple bounding boxes, each with a confidence score that reflects how likely it is that an object exists within the box. Each box includes the coordinates (x, y, width, height) and a class probability score.

Class Prediction: Along with the bounding boxes, YOLO predicts the class probabilities for each object, like "dog," "car," or "person." It multiplies these probabilities by the confidence scores to filter the most accurate predictions.

Non-Maximum Suppression (NMS): After initial predictions, YOLO applies Non-Maximum Suppression to remove overlapping boxes and keep only the highest-confidence boxes for each detected object.

Example Use Case
Consider a traffic monitoring system that uses YOLO for real-time object detection. The system can detect cars, pedestrians, and bicycles on the road:

Input: A video stream from a traffic camera.

C:\Users\mucah\OneDrive\Desktop\python\Object Detection (YOLO v11)\runs\detect\exp\adana teknofest.jpg
Output: Each frame is processed by the YOLO model, which detects objects in the frame and draws bounding boxes around vehicles, pedestrians, and bicycles. Each object is labeled, and a confidence score is displayed.

This setup allows the system to monitor traffic flow, detect anomalies like stopped vehicles, or analyze pedestrian crossings in real time.

**Why Use YOLO?**
Here are the primary reasons YOLO is widely used for object detection:
Speed: YOLO is much faster than most object detection algorithms, making it ideal for real-time applications.
Accuracy: YOLO has strong performance for detecting objects in complex scenes, especially when using its larger versions (e.g., YOLOv3, YOLOv5).
Simplicity: YOLO is end-to-end, meaning it processes an image in a single pass, unlike region-based methods that require multiple steps.
Versatility: YOLO can be applied to both video and still images, allowing it to detect objects in various media formats.

**RESULT**


C:\Users\mucah\OneDrive\Desktop\python\Object Detection (YOLO v11)\runs\detect\exp\adana teknofest.jpg
