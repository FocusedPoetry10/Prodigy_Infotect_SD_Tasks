import tkinter as tk
from tkinter import ttk

class TemperatureConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry("800x500")
        self.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        
        self.title_label = tk.Label(self, text="Temperature Converter", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)
        
        self.input_label = ttk.Label(self, text="Enter temperature:", background="#f0f0f0")
        self.input_label.pack(pady=5)
        
        self.input_entry = ttk.Entry(self, font=("Helvetica", 14))
        self.input_entry.pack(pady=5, padx=20, fill=tk.X)
        
        self.unit_label = ttk.Label(self, text="Select input unit:", background="#f0f0f0")
        self.unit_label.pack(pady=5)
        
        self.unit_var = tk.StringVar()
        self.unit_var.set("Celsius")
        
        self.unit_menu = ttk.Combobox(self, textvariable=self.unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Helvetica", 12))
        self.unit_menu.pack(pady=5, padx=20, fill=tk.X)
        
        self.convert_button = ttk.Button(self, text="Convert", command=self.convert_temperature, style="TButton")
        self.convert_button.pack(pady=20)

        self.result_label = tk.Label(self, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
        self.result_label.pack(pady=5)

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), background="#007bff", foreground="black", padding=10)
        style.configure("TCombobox", font=("Helvetica", 12))
        style.map("TButton", background=[('active', '#000000')])

    def convert_temperature(self):
        try:
            temp = float(self.input_entry.get())
            unit = self.unit_var.get()

            if unit == "Celsius":
                fahrenheit = (temp * 9/5) + 32
                kelvin = temp + 273.15
                result = f"Fahrenheit: {fahrenheit:.2f}\nKelvin: {kelvin:.2f}"
            elif unit == "Fahrenheit":
                celsius = (temp - 32) * 5/9
                kelvin = celsius + 273.15
                result = f"Celsius: {celsius:.2f}\nKelvin: {kelvin:.2f}"
            elif unit == "Kelvin":
                celsius = temp - 273.15
                fahrenheit = (celsius * 9/5) + 32
                result = f"Celsius: {celsius:.2f}\nFahrenheit: {fahrenheit:.2f}"

            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")

if __name__ == "__main__":
    app = TemperatureConverter()
    app.mainloop()
