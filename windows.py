import customtkinter as ctk
import tkinter as tk

from settings import *

import os
from utils import get_path as gp


class BaseWindow:
    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.window.title("TAP")
        self.window.geometry("800x600")

    def run(self) -> None:
        self.window.mainloop()


class UserAgreementWindow(BaseWindow):
    def __init__(self) -> None:
        super().__init__()

        greeting_label = ctk.CTkLabel(master=self.window,
                            text="Welcome!",
                            font=ctk.CTkFont(family="Helvetica",
                                            size=30, weight="bold"))
        greeting_label.pack(padx=10, pady=(40, 20))

        scrollable_frame = ctk.CTkScrollableFrame(master=self.window,
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

        add_task_button = ctk.CTkButton(master=self.window,
                                        text="I Agree",
                                        width=520,
                                        command=self.window_destroy)
        add_task_button.pack(pady=20)

    def window_destroy(self) -> None:
        self.window.destroy()
