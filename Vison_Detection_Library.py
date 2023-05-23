from utils import get_path as gp

import cv2
import os


def detect_face():
    model_path = os.path.join(gp.get_path(), "haarcascade_frontalface_default.xml")
    faceCascade = cv2.CascadeClassifier(model_path)

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # set Width
    cap.set(4, 480)  # set Height

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (64, 228, 254), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        img = cv2.flip(img, 1)
        cv2.imshow('video', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            break
        #TODO: add possibility to close the window using the cross

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_face()
