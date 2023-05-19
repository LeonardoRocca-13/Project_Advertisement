import os
import cv2


# getting the path of the current file
def get_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return path


def detect_face():
    # constructing the path to the Haar cascade model for face detection
    model_path = os.path.join(get_path(), "../Resources/haarcascade_frontalface_default.xml")
    faceCascade = cv2.CascadeClassifier(model_path)

    # accessing the default camera
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # set Width
    cap.set(4, 480)  # set Height

    while True:
        # reading a frame from the camera
        ret, img = cap.read()

        img = cv2.flip(img, 1)  # flip video image vertically

        # converting the image to grayscale for face detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detecting faces in the grayscale image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:
            # drawing a rectangle around each detected face
            cv2.rectangle(img, (x, y), (x + w, y + h), (64, 228, 254), 2)

        # displaying the video stream with the detected faces
        cv2.imshow('video', img)

        # waiting for the 'ESC' key to be pressed to exit the program
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # releasing the camera and closing all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_face()