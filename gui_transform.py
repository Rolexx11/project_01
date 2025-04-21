import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

class TransformGUI:
    def __init__(self, master):
        self.master = master
        master.title("Transform Plotter")

        self.label1 = tk.Label(master, text="Frequency:")
        self.label1.grid(row=0, column=0)

        self.entry1 = tk.Entry(master)
        self.entry1.grid(row=0, column=1)

        self.label2 = tk.Label(master, text="Amplitude:")
        self.label2.grid(row=1, column=0)

        self.entry2 = tk.Entry(master)
        self.entry2.grid(row=1, column=1)

        self.function_label = tk.Label(master, text="Select Function:")
        self.function_label.grid(row=2, column=0)

        self.function_var = tk.StringVar()
        self.function_var.set("Sin")  # Default selection
        self.function_menu = tk.OptionMenu(master, self.function_var, "Sin", "Cos", "Tan")
        self.function_menu.grid(row=2, column=1)

        self.transform_label = tk.Label(master, text="Select Transform:")
        self.transform_label.grid(row=3, column=0)

        self.transform_var = tk.StringVar()
        self.transform_var.set("Laplace")  # Default selection
        self.transform_menu = tk.OptionMenu(master, self.transform_var, "Laplace",
        "Fourier", "Z-Transform")
        self.transform_menu.grid(row=3, column=1)

        self.plot_button = tk.Button(master, text="Plot", command=self.plot_transform)
        self.plot_button.grid(row=4, columnspan=2)

    def plot_transform(self):
        try:
            frequency = float(self.entry1.get())
            amplitude = float(self.entry2.get())
            function = self.function_var.get()
            transform = self.transform_var.get()

            t = np.linspace(0, 1, 500)

            if function == "Sin":
                y = amplitude * np.sin(2 * np.pi * frequency * t)
                function_name = "Sin Wave"
            elif function == "Cos":
                y = amplitude * np.cos(2 * np.pi * frequency * t)
                function_name = "Cos Wave"
            elif function == "Tan":
                y = amplitude * np.tan(2 * np.pi * frequency * t)
                function_name = "Tan Wave"

            if transform == "Laplace":
                fft_y = np.fft.fft(y)
                plt.plot(np.fft.fftfreq(len(t)), fft_y.real, label='Real part')
                plt.plot(np.fft.fftfreq(len(t)), fft_y.imag, label='Imaginary part')
                plt.title("Laplace Transform of " + function_name)
                plt.xlabel('Frequency')
                plt.ylabel('Magnitude')
                plt.legend()
                plt.grid(True)
                plt.show()
            elif transform == "Fourier":
                fft_y = np.fft.fft(y)
                plt.plot(np.fft.fftfreq(len(t)), np.abs(fft_y))
                plt.title("Fourier Transform of " + function_name)
                plt.xlabel('Frequency')
                plt.ylabel('Magnitude')
                plt.grid(True)
                plt.show()
            elif transform == "Z-Transform":
                z_transform = np.fft.fft(y)
                plt.plot(np.abs(z_transform))
                plt.title("Z-Transform of " + function_name)
                plt.xlabel('Frequency')
                plt.ylabel('Magnitude')
                plt.grid(True)
                plt.show()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

def main():
    root = tk.Tk()
    my_gui = TransformGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()