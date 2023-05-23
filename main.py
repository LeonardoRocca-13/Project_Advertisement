import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

import cv2
import os

import Vison_Detection_Library as vdl
from utils import get_path as gp


DATA_FILE_PATH = "data"
USER_AGREEMENT_FILE_NAME = "user_agreement.txt"


# TODO: Implement a window class
def greeting_window():
    welcome_window = ctk.CTk()
    welcome_window.title("TAP")
    welcome_window.geometry("800x600")


    greeting_label = ctk.CTkLabel(master=welcome_window,
                            text="Welcome!",
                            font=ctk.CTkFont(family="Helvetica",
                                            size=30, weight="bold"))
    greeting_label.pack(padx=10, pady=(40, 20))

    scrollable_frame = ctk.CTkScrollableFrame(master=welcome_window,
                                            width=500, height=300)
    scrollable_frame.pack()

    title_label = ctk.CTkLabel(master=scrollable_frame,
                            text="User Agreement",
                            font=ctk.CTkFont(family="Helvetica",
                                                size=20, weight="bold"))
    title_label.pack(fill="x")

    # getting current file path
    current_path = gp.get_path()
    current_path = os.path.join(current_path, DATA_FILE_PATH)

    # using the current file path to get the path of the user agreement text
    user_agreement_path = os.path.join(current_path, USER_AGREEMENT_FILE_NAME)

    # importing a sample user agreement text to be displayed
    with open(user_agreement_path, "r") as file:
        user_agreement_text: str = file.read()
    
    # make the text fit the width of the frame and justify it

    user_agreement_label = ctk.CTkLabel(master=scrollable_frame,
                                        text=user_agreement_text,
                                        font=ctk.CTkFont(family="Helvetica",
                                                            size=15),
                                        wraplength=500,
                                        justify="left")

    user_agreement_label.pack(fill="x", pady=10)

    add_task_button = ctk.CTkButton(master=welcome_window,
                                    text="I Agree",
                                    width=520,
                                    command=welcome_window.destroy)
    add_task_button.pack(pady=20)


    welcome_window.mainloop()


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
    # while True:
    #     if not video_capture():
    #         video_capture.release()
    #         cv2.destroyAllWindows()
    #         break
    #     # Read a frame from the video capture
    #     ret, frame = video_capture.read()

    #     # Flip the frame horizontally
    #     frame_flipped = cv2.flip(frame, 1)

    #     # Convert the frame to RGB format
    #     frame_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)

    #     # Resize the frame to fit the Tkinter window
    #     frame_resized = cv2.resize(frame_rgb, (800, 600))

    #     # Convert the frame to an ImageTk format
    #     image = Image.fromarray(frame_resized)
    #     image_tk = ImageTk.PhotoImage(image)

    #     # Update the canvas with the new frame
    #     canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
    #     canvas.image = image_tk

    #     # Update the Tkinter GUI
    #     webcam_window.update()

    #     # Break the loop if the user presses the 'q' key
    #     # k = cv2.waitKey(30) & 0xff
        
    #     k = cv2.waitKey(30) & 0xff
    #     if k == 27:  # press 'ESC' to quit
    #         # Release the video capture and destroy the OpenCV windows
    #         video_capture.release()
    #         cv2.destroyAllWindows()
    #         break

    # webcam_window.mainloop()


if __name__ == "__main__":
    greeting_window()
    webcam_window()