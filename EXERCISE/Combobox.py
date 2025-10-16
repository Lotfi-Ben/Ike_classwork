import tkinter as tk
from tkinter import ttk

def sumbit():
    if text_string.get() == "This option":
        label_string.set("Nice.")
    elif text_string.get() == "That option":
        label_string.set("Woah, calm down.")
    elif text_string.get() == "A third option?!":
        label_string.set("ANOTHER OPTION!?")
    else:
        label_string.set("Cool")

def update_combobox():
    new_values = ["6", "2", "93"]
    combox['values'] = new_values

#window
window = tk.Tk()
window.title("Combox")
window.geometry("400x400")

#frame
frame = ttk.Frame(window)
frame.pack()

#combobox
text_string = tk.StringVar()
combo = ttk.Combobox(frame, textvariable=text_string,values=["This option", "That option", "A third option?!"])
combo.pack()

#anotherbox
options = tk.StringVar()
combox = ttk.Combobox(frame, textvariable=options,postcommand=update_combobox)
combox.pack()

#button
button = ttk.Button(window, text="submit", command=sumbit)
button.pack()

#label
label_string = tk.StringVar()
label = ttk.Label(window, textvariable=label_string, font="Calibri 23 bold")
label.pack()

#run
window.mainloop()