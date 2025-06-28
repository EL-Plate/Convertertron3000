import customtkinter


customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark

app = customtkinter.CTk()
app.geometry("800x800")


def button_function():
    customtkinter.set_default_color_theme("blue")


custom_button = customtkinter.CTkButton(master=app, text="Colour Changer", command=button_function)
custom_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


app.mainloop()
