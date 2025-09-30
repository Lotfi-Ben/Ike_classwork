import tkinter as tk
from tkinter import ttk

def set_label():
    edited_label = label.cget("text") + "_edited"
    output_string.set(edited_label)

#window
window = tk.Tk()
window.title("Label")
window.geometry("400x400")

#style
style = ttk.Style()
style.configure("Custom.TLabel", foreground="red", font=("Comic Sans MS", 24))

#label
label = ttk.Label(window, text="Label", style="Custom.TLabel", justify="center")
label.configure(underline=0)
label.pack(pady=20)

#button
button = ttk.Button(window, text="Edit", command=set_label)
button.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(window, style="Custom.TLabel", textvariable=output_string)
output_label.pack(pady=10)

window.mainloop()
