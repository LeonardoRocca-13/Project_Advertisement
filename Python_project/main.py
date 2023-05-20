import customtkinter as ctk
import cv2
import tkinter as tk
from PIL import Image, ImageTk


# TODO: Implement a window class & create soup object that gets a flight ticket
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

    # creating a sample user agreement text to be displayed, and allowing the face to be scanned in order to get age, gender and mood
    user_agreement_text = """By using this application, you agree to the following terms and conditions:

1. You must be at least 18 years old to use this application.
2. You agree to abide by all applicable laws and regulations.
3. Your personal information may be collected and used as described in our privacy policy.
4. We are not responsible for any damages or losses incurred while using this application.
5. You are solely responsible for the content you upload or share through this application.

Please read this agreement carefully before using the application.
If you do not agree with any of these terms, please do not use the application.
--------------------------------------------------------------------------------------------------------

Privacy Policy

We collect information about you when you use this application.
This information is used to provide a better user experience and improve our services.
We may share your personal information with third parties for marketing purposes.
You can opt out of these communications at any time by contacting
us at contact@samplecompany.com
--------------------------------------------------------------------------------------------------------

Contact Us

If you have any questions about this agreement, please contact
us at contact@samplecompany.com."""

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
    video_capture = cv2.VideoCapture(0)

    # Continuously capture frames from the video feed
    # while True:
    i = 0
    while video_capture.isOpened():
        # Read a frame from the video capture
        for i in range(100):
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
            if cv2.waitKey(1) & 0xFF == ord('q'):
            # if k == 27:  # press 'ESC' to quit
                break

    # Release the video capture and destroy the OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

    webcam_window.mainloop()


if __name__ == "__main__":
    greeting_window()
    webcam_window()