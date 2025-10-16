import tkinter as tk
from tkinter import ttk

def get_button1_text():
    print("Button 2")

def get_button2_text():
    print("Button 1")

#window
window = tk.Tk()
window.title("button")
window.geometry("300x150")

#labelFrame
frame = ttk.LabelFrame(window, text="My Choice", padding=10)
frame.pack(padx=20, pady=20, fill="both", expand=True)

#buttons
button = ttk.Button(master=frame, text="Button", command=get_button1_text)
button_2 = ttk.Button(master=frame, text="Button 2", command=get_button2_text)

button.pack(pady=5)
button_2.pack(pady=5)

window.mainloop()
