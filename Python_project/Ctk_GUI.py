import customtkinter as ctk


def button_function():
    advertisement = "This is a sample advertisement."
    advertisement_label.configure(text=advertisement)

window = ctk.CTk()
window.title("TAP")
window.geometry("800x500")

greeting_label = ctk.CTkLabel(window,
                            text="Hello User!",
                            font=("Helvetica Bold", 21))
greeting_label.pack(pady=10)

button = ctk.CTkButton(window,
                     text="Get Sample advertisement",
                     command=button_function)
button.pack(pady=10)

advertisement_label = ctk.CTkLabel(window,
                                 text="",
                                 font=("Helvetica Bold", 21))
advertisement_label.pack(pady=10)

# get a sample flight ticket by pressing a button
# visualize the flight ticket on the left of the window (if not ok then a retry button)
# get a button to submit the flight ticket with all the other information

window.mainloop()