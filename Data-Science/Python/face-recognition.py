# Detect faces from a live video feed, such as a CCTV camera in a hospital. 
# References: https://github.com/ageitgey/face_recognition based on OpenCV dlib (trained with HOG & CNN)
# https://pyimagesearch.com/2021/04/19/face-detection-with-dlib-hog-and-cnn/ 

import cv2
import face_recognition

# Initialize video capture (replace '0' with your video feed or file path)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Draw bounding boxes around detected faces
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
video_capture.release()
cv2.destroyAllWindows()
