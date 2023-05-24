import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

import libraries.vison_detection as vdl

from libraries.windows import UserAgreementWindow
import libraries.text_generation


def greeting_window():
    greeting_window = UserAgreementWindow()
    greeting_window.run()


def webcam_window():
    bio_info = vdl.capture_frame()
    return bio_info


def flight_window():
    flight_window = ctk.CTk()
    flight_window.title("Flight")
    flight_window.geometry("800x600")
    flight_window.mainloop()
    # ottenimento biglietto simulato
    # funzione get_flight
    # get_flight(infos)


def ad_window(infos: tuple):
    ...
    # Return the ad


def get_ad(infos: tuple):
    ...


def get_product():
    ...


def main():
    greeting_window()
    infos = webcam_window()
    ad_window(infos)


if __name__ == "__main__":
    main()
