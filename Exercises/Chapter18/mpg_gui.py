#!/usr/bin/env python3

from mpg import MPG
import tkinter as tk
from tkinter import ttk, messagebox

class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()
        self.mpg = MPG()
        self.message = ""

        # Define string variables for text entry fields
        self.miles = tk.StringVar()
        self.gasUsed = tk.StringVar()
        self.milesPerGallon = tk.StringVar()

        # Display the grid of components
        ttk.Label(self, text="Miles Driven:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.miles).grid(
            column=1, row=0)
        
        ttk.Label(self, text="Gallons of Gas Used:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.gasUsed).grid(
            column=1, row=1)
        
        ttk.Label(self, text="Miles Per Gallon:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.milesPerGallon, state="readonly").grid(
            column=1, row=2)

        self.make_buttons()

        # Add padding to all components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)
    
    def make_buttons(self):
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        ttk.Button(buttonFrame, text="Calculate", command=self.calculate).grid(column=1, row=0, padx=0)
    
    def calculate(self):
        self.message = ""

        self.mpg.milesDriven = self.get_float(self.miles.get(), "Miles Driven")
        self.mpg.gallonsOfGasUsed = self.get_float(self.gasUsed.get(), "Gallons of Gas")

        if self.message == "":
            self.milesPerGallon.set(self.mpg.calculate_mpg())
        else:
            messagebox.showerror("Error", self.message)

    def get_float(self, val, fieldname):
        try:
            return float(val)
        except ValueError:
            self.message += f"{fieldname} must be a valid number.\n"

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Miles Per Gallon Calculator")
    MyFrame(root)
    root.mainloop()
