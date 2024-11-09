import cv2
import numpy as np

cap1 = cv2.VideoCapture("raw3.avi")
cap2 = cv2.VideoCapture("raw3.avi") # Replace with the path to your second video

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret2:
        break

    # Get the dimensions of the frames
    height1, width1 = frame1.shape[:2]
    height2, width2 = frame2.shape[:2]

    # Resize the second video to fit below the first video and in the right half of the frame
    resized_frame2 = cv2.resize(frame2, (int(height1 * width2 / height2), height1))

    # Create a blank space on the right side of the first video
    blank_space = np.zeros((height1, int(width1 / 2), 3), dtype=np.uint8)

    # Combine the first video, the blank space, and the resized second video
    new_frame = np.vstack((frame1, blank_space, resized_frame2))

    # Put text in the blank space
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(new_frame, 'Your Text Here', (10, int(height1 / 2)), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the modified frame
    cv2.imshow('Video', new_frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
