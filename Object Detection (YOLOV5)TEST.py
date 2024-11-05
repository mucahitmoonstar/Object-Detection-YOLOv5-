import torch
import cv2
from PIL import Image
from pathlib import Path

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_objects_in_image(image_path):
    # Open image
    image = Image.open(image_path)
    
    # Run inference
    results = model(image)
    
    # Print results
    results.print()  # Print results to console
    results.show()   # Display results in a new window
    
    # Save results if needed
    results.save()  # Saves results to 'runs/detect/exp' folder by default

def detect_objects_in_video(video_path, output_path='output_video.avi'):
    # Open video file
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Define video writer to save output
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to PIL Image
        pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        # Run inference
        results = model(pil_frame)
        
        # Extract the result image
        result_img = results.render()[0]
        
        # Convert the image back to BGR for OpenCV
        result_img = cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR)
        
        # Write frame to output video
        out.write(result_img)
        
        # Display frame (optional)
        cv2.imshow('YOLOv5 Detection', result_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Example usage:
# Detect objects in an image
detect_objects_in_image("C:\\Users\\mucah\\OneDrive\\Desktop\\adana teknofest.jpg")


# Detect objects in a video
#detect_objects_in_video('path/to/your/video.mp4')
