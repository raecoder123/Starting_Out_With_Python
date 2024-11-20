import tkinter as tk
from tkinter import messagebox

# Function to convert Fahrenheit to Celsius
def convert():
    # Get the input from the entry box
    fah = entry.get()
    # Try to convert it to a float
    try:
        fah = float(fah)
        # Perform the conversion
        cels = (fah - 32) * 5 / 9
        # Show the result in a message box
        messagebox.showinfo("Results", str(fah) + " Fahrenheit is " + str(cels) + " Celsius.")
    except ValueError:
        # Show an error if the input is not a number
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Fahrenheit to Celsius Converter")

# Create
