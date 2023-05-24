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
    infos = vdl.capture_frame()
    return infos


def ad_window(infos: tuple):
    ad_window = ctk.CTk()
    ad_window.title("Advertisement")
    ad_window.geometry("800x600")
    ad_window.mainloop()
    # ottenimento biglietto simulato
    # funzione get_ad
    # get_ad(infos)


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
