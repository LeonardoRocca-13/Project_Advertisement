import customtkinter as ctk

import os

# from utils.settings import USER_AGREEMENT_FILE_NAME, RESOURCES_FOLDER_NAME
# from utils.get_path import get_path
from libraries.utils.settings import USER_AGREEMENT_FILE_NAME, RESOURCES_FOLDER_NAME
from libraries.utils.get_path import get_path


class BaseWindow:
    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.window.title("TAP")
        self.window.geometry("800x600")

    def add_label(self, label_master, label_text,
                  font_size, font_weight, 
                  label_padx=0, label_pady=0, 
                  is_label_wrap=False) -> None:
        label_font = ctk.CTkFont(family="Helvetica", size=font_size, weight=font_weight)
        if not is_label_wrap:
            new_label = ctk.CTkLabel(master=label_master,
                                    text=label_text,
                                    font=label_font)
        else:
            new_label = ctk.CTkLabel(master=label_master,
                                    text=label_text,
                                    font=label_font,
                                    wraplength=500,
                                    justify="left")

        new_label.pack(padx=label_padx, pady=label_pady)

    def add_button(self, button_master, button_text,
                   button_width, button_command,
                   button_padx=0, button_pady=0) -> None:
        new_button = ctk.CTkButton(master=button_master,
                                   text=button_text,
                                   width=button_width,
                                   command=button_command)
        new_button.pack(padx=button_padx, pady=button_pady)

    def run(self) -> None:
        self.window.mainloop()


class UserAgreementWindow(BaseWindow):
    def __init__(self) -> None:
        super().__init__()
        self.user_agreement_text = self.get_user_agreement()

        # greeting label
        self.add_label(label_master=self.window,
                       label_text="Welcome!",
                       font_size=30, font_weight="bold",
                       label_padx=10, label_pady=(40, 20))

        scrollable_frame = ctk.CTkScrollableFrame(master=self.window,
                                                width=500, height=300)
        scrollable_frame.pack()

        # user agreement Title
        self.add_label(label_master=scrollable_frame,
                       label_text="User Agreement",
                       font_size=20, font_weight="bold")
        
        # user agreement text
        self.add_label(label_master=scrollable_frame,
                       label_text=self.user_agreement_text,
                       font_size=15, font_weight="normal",
                       is_label_wrap=True)

        # Agreement button
        self.add_button(button_master=self.window,
                        button_text="I Agree",
                        button_width=520,
                        button_command=self.window_destroy,
                        button_pady=20)

    @staticmethod
    def get_user_agreement() -> str:
        """Get the text of the user agreement file"""
        current_path = get_path()
        user_agreement_path = os.path.join(current_path, RESOURCES_FOLDER_NAME, USER_AGREEMENT_FILE_NAME)
        with open(user_agreement_path, "r") as file:
            user_agreement_text: str = file.read()
        
        return user_agreement_text

    def window_destroy(self) -> None:
        self.window.destroy()

if __name__ == "__main__":
    user_agreement_window = UserAgreementWindow()
    user_agreement_window.run()