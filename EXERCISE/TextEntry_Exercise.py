import tkinter as tk
from tkinter import ttk

def submit_text():
    edited_text = string_var.get() + "_Edited"
    output_label.config(text=edited_text)

#window
window = tk.Tk()
window.title("titlecard")
window.geometry("400x400")

#entry
string_var = tk.StringVar()
Text_entry = ttk.Entry(window, textvariable=string_var, font=("Comic Sans MS", 24, "bold"), foreground="blue", justify="center", show="*")
Text_entry.pack(pady=10)

#button
submit_button = ttk.Button(window, text="Submit", command=submit_text)
submit_button.pack(pady=10)

#label
output_label = ttk.Label(window, text="", font=("Comic Sans MS", 20))
output_label.pack(pady=10)

#run
window.mainloop()
