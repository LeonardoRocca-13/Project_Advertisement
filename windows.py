import customtkinter as ctk


class BaseWindow:
    def __init__(self) -> None:
        self.window = ctk.CTk()
        self.window.title("TAP")
        self.window.geometry("800x600")

    def run(self) -> None:
        self.window.mainloop()
