import customtkinter as ctk

def greeting_window():
    welcome_window = ctk.CTk()
    welcome_window.title("TAP")
    welcome_window.geometry("800x500")


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

if __name__ == "__main__":
    greeting_window()