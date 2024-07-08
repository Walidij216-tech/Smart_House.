import cv2

# Load trained data
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def recognize_faces():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # 0 indicates the first camera connected (usually the Raspberry Pi camera)

    # Names corresponding to each detected face
    person_names = ["walid", "yasmin"]

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Track the number of faces detected
        detected_persons = 0

        # Process each face found
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Check if within the range of detected persons
            if detected_persons < len(person_names):
                # Draw name label
                cv2.putText(frame, person_names[detected_persons], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            else:
                # More faces detected than expected
                cv2.putText(frame, 'Unknown', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            detected_persons += 1

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Exit loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_faces()
