import tkinter as tk
from tkinter import ttk

def update_label():
    if bool_var.get():
        string_var.set("I'm very happy for you")
    else:
        string_var.set("I'm very sad for you")

#window
window = tk.Tk()
window.title("checkbutton")
window.geometry("400x400")

#checkbox
bool_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(window,variable=bool_var,text="are you happy",onvalue=True,offvalue=False,command=update_label)
checkbox.pack()

#label
string_var = tk.StringVar()
label = ttk.Label(window,textvariable=string_var,font=("Comic Sans MS",16,"bold"))
label.pack()

#run
window.mainloop()
