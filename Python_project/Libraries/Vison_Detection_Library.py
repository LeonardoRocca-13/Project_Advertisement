import os
import cv2
import time
import numpy as np
from deepface import DeepFace


# getting the path of the current file
def get_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return path


def extract_info(frame: cv2, infos: dict):
    result = DeepFace.analyze(frame, actions=['gender', 'age', 'emotion'], enforce_detection=False, silent=True)

    infos['age'].append(int(result[0]['age']))
    infos['gender'].append(result[0]['dominant_gender'])
    infos['emotion'].append(result[0]['dominant_emotion'])


def detect_face():
    # Get the Haar cascade model for face detection
    model_path = os.path.join(get_path(), "../Resources/haarcascade_frontalface_default.xml")
    faceCascade = cv2.CascadeClassifier(model_path)

    # Accessing the default camera
    capture = cv2.VideoCapture(0)  # 0 = default camera
    capture.set(3, 640)  # set Width
    capture.set(4, 480)  # set Height

    # Define the information to extract from the face
    infos = {
        'age': [],
        'gender': [],
        'emotion': []
    }

    # Define the maximum number of seconds to detect faces
    set_max_seconds = 10
    start = time.time()

    # Start the loop only when the camera is opened
    while capture.isOpened():
        ret, frame = capture.read()
        # if the frame is read correctly, ret is True
        if ret:

            # Flip the frame vertically
            frame = cv2.flip(frame, 1)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image

            extract_info(frame, infos)

            print(infos)

            faces = faceCascade.detectMultiScale(
                gray_frame,
                scaleFactor=1.2,
                minNeighbors=6,
                minSize=(30, 30)
            )

            for (x, y, w, h) in faces:
                # drawing a rectangle around each detected face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (64, 228, 254), 2)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xff == 27 or (time.time() - start) > set_max_seconds:
                break
        else:
            break

    # When everything done, release the capture
    capture.release()
    cv2.destroyAllWindows()

    age = int(np.mean(infos['age']))
    gender = max(set(infos['gender']), key=infos['gender'].count)
    emotion = max(set(infos['emotion']), key=infos['emotion'].count)
    print(age, gender, emotion)


if __name__ == "__main__":
    detect_face()
