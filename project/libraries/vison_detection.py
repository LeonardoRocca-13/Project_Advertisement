from deepface import DeepFace
import numpy as np
import time
import cv2
import os

from libraries.utils.get_path import get_path
from libraries.utils.settings import HAARCASCADE_FILE_NAME, RESOURCES_FOLDER_NAME


def capture_frame():
    info = []
    # Open the default camera
    capture = cv2.VideoCapture(0)

    # Set the maximum duration to capture frames (in seconds)
    set_max_seconds = 15
    start = time.time()

    while capture.isOpened():
        # Read a frame from the camera
        ret, frame = capture.read()
        if ret:
            # Detect faces in the frame and show them
            detect_face(frame)

            analyze_face(frame, info)

            # Flip the frame horizontally
            frame = cv2.flip(frame, 1)

            # Display the frame
            cv2.imshow('frame', frame)

            # Check if the 'Esc' key is pressed or the maximum duration is reached
            if cv2.waitKey(1) & 0xff == 27 or (time.time() - start) > set_max_seconds:
                break
        else:
            break

    # Release the camera and close all windows
    capture.release()
    cv2.destroyAllWindows()

    # create_report(info)
    bio_info = extract_info(info)

    return bio_info


def detect_face(frame: cv2):
    # Get the path to the model file
    model_path = os.path.join(get_path(), RESOURCES_FOLDER_NAME, HAARCASCADE_FILE_NAME)

    # Create a CascadeClassifier object for face detection
    faceCascade = cv2.CascadeClassifier(model_path)

    # Convert the frame to grayscale and detect faces
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.2,
        minNeighbors=8,
        minSize=(30, 30)
    )

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (64, 228, 254), 2)


def analyze_face(frame: cv2, info: list):
    # Analyze the face in the frame and append the analysis results to the info list
    analysis_result = DeepFace.analyze(frame, actions=['gender', 'age', 'emotion'], enforce_detection=False, silent=True)
    info.append(analysis_result)


def extract_info(info: list):
    # Create a dictionary to store the extracted information
    bio_info = []
    result = {
        'age': [],
        'gender': [],
        'emotion': []
    }

    # Extract age, gender, and emotion from each frame in the info dictionary
    for frame in info:
        result['age'].append(frame[0]['age'])
        result['gender'].append(frame[0]['dominant_gender'])
        result['emotion'].append(frame[0]['dominant_emotion'])

    # Calculate the mean age, most frequent gender, and most frequent emotion
    bio_info.append(int(np.median(result['age'])))
    bio_info.append(max(set(result['gender']), key=result['gender'].count))
    bio_info.append(max(set(result['emotion']), key=result['emotion'].count))

    # Return the extracted and calculated information
    return tuple(bio_info)


def create_report(info: list):
    with open(f'report_{time.time()}.txt', 'w') as report:
        report.write('Report of the analysis of the video\n\n')

        # Iterate over each frame in the info list
        for index, frame in enumerate(info):
            report.write(f'Frame analyzed [{index}]:\n\n')

            # Iterate over the key-value pairs in the frame dictionary
            for key, value in frame[0].items():
                report.write(f'{key}: {value}\n\n')
