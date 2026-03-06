import cv2 
import threading
from alarm import alarm

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    "haarcascade/haarcascade_frontalface_default.xml"
)

# Start webcam
cap = cv2.VideoCapture(0)

alarm_triggered = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # If face detected
    if len(faces) > 0:
        if not alarm_triggered:
            alarm_triggered = True
            threading.Thread(target=alarm).start()
    else:
        alarm_triggered = False


     # Draw rectangle around face
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame, (x, y),
            (x + w, y + h),
            (0, 255, 0), 2
        )


    cv2.imshow("Face Detection Alarm", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()