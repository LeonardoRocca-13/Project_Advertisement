import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

import cv2
import os

import Vison_Detection_Library as vdl
from utils import get_path as gp

from windows import UserAgreementWindow


def greeting_window():
    greeting_window = UserAgreementWindow()
    greeting_window.run()


# Creating a rough draft of the window that will be used to scan the users face
def webcam_window():
    webcam_window = ctk.CTk()
    webcam_window.title("TAP")
    webcam_window.geometry("800x600")

    webcam_label = ctk.CTkLabel(master=webcam_window,
                                text="Webcam",
                                font=ctk.CTkFont(family="Helvetica",
                                                 size=30, weight="bold"))
    webcam_label.pack(padx=10, pady=(40, 20))

    
    # Create a canvas to display the video feed
    canvas = tk.Canvas(webcam_window, width=800, height=600)
    canvas.pack()

    # Start capturing and displaying the video frames
    
    # Use OpenCV to capture video from the webcam
    # video_capture = cv2.VideoCapture(0)
    video_capture = vdl.detect_face()

    #TODO: Fix the issue with the video capture (integrated with the face detection library)
    # As for now they are 2 separate windows

    # Continuously capture frames from the video feed
    while True:
        if not video_capture():
            video_capture.release()
            cv2.destroyAllWindows()
            break
        # Read a frame from the video capture
        ret, frame = video_capture.read()

        # Flip the frame horizontally
        frame_flipped = cv2.flip(frame, 1)

        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)

        # Resize the frame to fit the Tkinter window
        frame_resized = cv2.resize(frame_rgb, (800, 600))

        # Convert the frame to an ImageTk format
        image = Image.fromarray(frame_resized)
        image_tk = ImageTk.PhotoImage(image)

        # Update the canvas with the new frame
        canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        canvas.image = image_tk

        # Update the Tkinter GUI
        webcam_window.update()

        # Break the loop if the user presses the 'q' key
        # k = cv2.waitKey(30) & 0xff
        
        k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            # Release the video capture and destroy the OpenCV windows
            video_capture.release()
            cv2.destroyAllWindows()
            break

    webcam_window.mainloop()


def testing_window_facescan():
    webcam_window = ctk.CTk()
    webcam_window.title("TAP")
    webcam_window.geometry("800x600")

    webcam_label = ctk.CTkLabel(master=webcam_window,
                                text="Webcam",
                                font=ctk.CTkFont(family="Helvetica",
                                                 size=30, weight="bold"))
    webcam_label.pack(padx=10, pady=(40, 20))

    
    # Create a canvas to display the video feed
    canvas = tk.Canvas(webcam_window, width=800, height=600)
    canvas.pack()

    model_path = os.path.join(gp.get_path(), "haarcascade_frontalface_default.xml")
    faceCascade = cv2.CascadeClassifier(model_path)

    cap = cv2.VideoCapture(0)
    cap.set(3, 800)  # set Width
    cap.set(4, 600)  # set Height

    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
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

        cv2.imshow('video', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            break
        #TODO: add possibility to close the window using the cross

    cap.release()
    cv2.destroyAllWindows()
    webcam_window.mainloop()


def get_ad():
    ad_window = ctk.CTk()
    ad_window.title("Advertisement")
    ad_window.geometry("800x600")
    ad_window.mainloop()


def main():
    greeting_window()
    # testing_window_facescan()
    # webcam_window()
    # get_ad()


if __name__ == "__main__":
    main()
