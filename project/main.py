import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

import cv2
import os

# import libraries.vison_detection as vdl
from libraries.windows import UserAgreementWindow
# from libraries.utils.get_path import get_path


def greeting_window():
    greeting_window = UserAgreementWindow()
    greeting_window.run()


def get_ad():
    ad_window = ctk.CTk()
    ad_window.title("Advertisement")
    ad_window.geometry("800x600")
    ad_window.mainloop()


def main():
    greeting_window()
    # webcam_window()
    # get_ad()


if __name__ == "__main__":
    main()
