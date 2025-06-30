import customtkinter


customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark

app = customtkinter.CTk()
app.title("ConverterTron 3000")
app.geometry("800x800")


def clear_temp_entry():
    celsius_entry.delete(0, len(celsius_entry.get()))
    fahrenheit_entry.delete(0, len(fahrenheit_entry.get()))
    conversion.configure(text="")


tabs = customtkinter.CTkTabview(master=app)
tabs.pack(pady=10)

temperature_tab = tabs.add("Celsius/Fahrenheit")
Weight_tab = tabs.add("Freedom Units/Metric")


def celsius_fahrenheit_function():
    if not celsius_entry.get() and not fahrenheit_entry.get():
        conversion.configure(text="Please enter an integer into one of the temperature fields")
    elif celsius_entry.get() and fahrenheit_entry.get():
        conversion.configure(text=f"Please only enter one temperature")
    elif celsius_entry.get() and not fahrenheit_entry.get():
        celsius = celsius_entry.get()
        conversion.configure(text=f"{round((int(celsius) * 1.8) + 32, 2)}")
    else:
        fahrenheit = fahrenheit_entry.get()
        conversion.configure(text=f"{round((int(fahrenheit) - 32) * 1.8, 2)}")


conversion = customtkinter.CTkLabel(master=temperature_tab, text="", font=("Helvetica", 18))
conversion.pack(pady=10)

celsius_entry = customtkinter.CTkEntry(master=temperature_tab, placeholder_text="Celsius")
celsius_entry.pack(pady=10)

fahrenheit_entry = customtkinter.CTkEntry(master=temperature_tab, placeholder_text="Fahrenheit")
fahrenheit_entry.pack(pady=10)

temperature_submit = customtkinter.CTkButton(master=temperature_tab, text="Submit", command=celsius_fahrenheit_function)
temperature_submit.pack(pady=10)

temperature_clear = customtkinter.CTkButton(master=temperature_tab, text="Clear", command=clear_temp_entry)
temperature_clear.pack(pady=5)

app.mainloop()
