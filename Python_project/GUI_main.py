import tkinter as tk
from tkinter import ttk


def button_function():
    advertisement = "This is a sample advertisement."
    advertisement_label.config(text=advertisement)


window = tk.Tk()
window.title("TAP")
window.geometry("800x600")

# text label
greeting_label = ttk.Label(window,
                  text="Hello User!",
                  font=("Helvetica Bold", 21))
greeting_label.pack(pady=10)

# button
button = ttk.Button(window,
                    text="Get Sample advertisement",
                    command=button_function)
button.pack(pady=10)

# advertisement label
advertisement_label = ttk.Label(window,
                                text="",
                                font=("Helvetica Bold", 21))
advertisement_label.pack(pady=10)

window.mainloop()