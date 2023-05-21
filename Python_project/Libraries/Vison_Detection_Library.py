import os
import cv2
import time
import numpy as np
from deepface import DeepFace


def get_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return path


def extract_info(frame: cv2, log_infos: dict):
    result = DeepFace.analyze(frame, actions=['gender', 'age', 'emotion'], enforce_detection=False, silent=True)

    log_infos['age'] = int(result[0]['age'])
    log_infos['gender'] = result[0]['dominant_gender']
    log_infos['emotion'] = result[0]['dominant_emotion']


def detect_face():
    model_path = os.path.join(get_path(), "../Resources/haarcascade_frontalface_default.xml")
    faceCascade = cv2.CascadeClassifier(model_path)

    with cv2.VideoCapture(0) as capture:
        capture.set(3, 640)
        capture.set(4, 480)

        log_infos = {'age': [], 'gender': [], 'emotion': []}

        set_max_seconds = 10
        start = time.time()

        while capture.isOpened():
            ret, frame = capture.read()

            if ret:
                frame = cv2.flip(frame, 1)
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                extract_info(frame, log_infos)

                faces = faceCascade.detectMultiScale(
                    gray_frame,
                    scaleFactor=1.2,
                    minNeighbors=6,
                    minSize=(30, 30)
                )

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (64, 228, 254), 2)

                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xff == 27 or (time.time() - start) > set_max_seconds:
                    break
            else:
                break

    person_data = {'age': int(np.mean(log_infos['age'])),
                   'gender': max(set(log_infos['gender']), key=log_infos['gender'].count),
                   'emotion': max(set(log_infos['emotion']), key=log_infos['emotion'].count)}

    return person_data, log_infos


if __name__ == "__main__":
    info, log = detect_face()
    print(info)
