import cv2

# Load the video file
cap = cv2.VideoCapture("put.mp4")

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, 30.0, (1920, 1080))

# Loop over the frames of the video
while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was successfully read
    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Write the grayscale frame to the output video
        out.write(gray)
    else:
        # If the frame was not successfully read, break the loop
        break

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
