import customtkinter as ctk
from libraries.utils.settings import USER_AGREEMENT_FILE_NAME, RESOURCES_FOLDER_NAME
from libraries.utils.get_path import get_path
import os


class BaseWindow:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("TAP")
        self.window.geometry("800x600")

    @staticmethod
    def add_label(label_master, label_text, font, label_padx=0, label_pady=0, is_label_wrap=False):
        label_font = ctk.CTkFont(*font)
        if not is_label_wrap:
            label = ctk.CTkLabel(master=label_master, text=label_text, font=label_font)
        else:
            label = ctk.CTkLabel(master=label_master, text=label_text, font=label_font, wraplength=500, justify="left")
        label.pack(padx=label_padx, pady=label_pady)
        return label

    @staticmethod
    def add_button(button_master, button_text, button_width, button_command, button_padx=0, button_pady=0):
        button = ctk.CTkButton(master=button_master, text=button_text, width=button_width, command=button_command)
        button.pack(padx=button_padx, pady=button_pady)
        return button

    def run(self):
        self.window.mainloop()


class UserAgreementWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.user_agreement_text = self.get_user_agreement()

        self.add_label(
            label_master=self.window,
            label_text="Welcome!",
            font=("Helvetica", 30, "bold"),
            label_padx=10,
            label_pady=(40, 20)
        )

        scrollable_frame = ctk.CTkScrollableFrame(master=self.window)
        scrollable_frame.configure(width=500, height=300)
        scrollable_frame.pack()

        self.add_label(
            label_master=scrollable_frame,
            label_text="User Agreement",
            font=("Helvetica", 20, "bold")
        )

        self.add_label(
            label_master=scrollable_frame,
            label_text=self.user_agreement_text,
            font=("Helvetica", 15, "normal"),
            is_label_wrap=True
        )

        self.add_button(
            button_master=self.window,
            button_text="I Agree",
            button_width=520,
            button_command=self.window_destroy,
            button_pady=20
        )

    @staticmethod
    def get_user_agreement():
        current_path = get_path()
        user_agreement_path = os.path.join(current_path, RESOURCES_FOLDER_NAME, USER_AGREEMENT_FILE_NAME)
        with open(user_agreement_path, "r") as file:
            user_agreement_text = file.read()

        return user_agreement_text

    def window_destroy(self):
        self.window.destroy()


class FlightWindow(BaseWindow):
    def __init__(self, flight_info, current_location, destination):
        super().__init__()
        self.flight_info = flight_info
        self.current_location = current_location
        self.destination = destination

        self.add_label(
            label_master=self.window,
            label_text="Scan your ticket",
            font=("Helvetica", 30, "bold"),
            label_padx=10,
            label_pady=(40, 20)
        )

        self.scan_button = self.add_button(
            button_master=self.window,
            button_text="Scan",
            button_width=520,
            button_command=self.successful_scan,
            button_pady=20
        )

    def successful_scan(self):
        self.scan_button.destroy()

        self.add_label(
            label_master=self.window,
            label_text="Ticket scanned successfully!",
            font=("Helvetica", 20, "bold"),
            label_padx=10,
            label_pady=20
        )

        display_text = f"Your flight information:\n\n" \
                       f"Flight duration: {self.flight_info[0]}\n" \
                       f"Boarding time: {self.flight_info[1]}\n" \
                       f"Destination: {self.destination[0]}, {self.destination[1]}\n" \
                       f"Airline: {self.flight_info[2]}\n"

        self.add_label(
            label_master=self.window,
            label_text=display_text,
            font=("Helvetica", 20, "normal"),
            label_padx=10,
            label_pady=(10, 12)
        )

        self.add_label(
            label_master=self.window,
            label_text=f"Current city: {self.current_location[0]}, {self.current_location[1]}",
            font=("Helvetica", 20, "normal"),
            label_padx=10,
            label_pady=(20, 10)
        )

        self.add_button(
            button_master=self.window,
            button_text="Keep going",
            button_width=520,
            button_command=self.window.destroy,
            button_pady=20
        )


class AdWindow(BaseWindow):
    def __init__(self, ad_text):
        super().__init__()

        self.add_label(
            label_master=self.window,
            label_text=f'Sample ad:\n\n{ad_text}',
            font=("Helvetica", 30, "normal"),
            label_padx=10,
            label_pady=(60, 10),
            is_label_wrap=True
        )
