import tkinter as tk
from tkinter import ttk
from numpy import number

#window
window = tk.Tk()
window.title("Spinbox")
window.geometry("400x400")

#spinbox
int_var = tk.IntVar()
spinbox = ttk.Spinbox(window, from_=0, to=100, increment=0.1, textvariable= int_var, font = "calibri 24 bold")
spinbox.pack()

#textspinbox
subjects =  ["Maths", "English", "Science", "Computing", "Latin", "Arabic", "Social Studies", "Sports Science"]
textbox = ttk.Spinbox(window, values=subjects, wrap=True)
#textbox.pack()

#style
style = ttk.Style()
style.configure("Custom.TLabel", foreground="blue", font=("Comic Sans MS", 24))

#frame
frame = ttk.Frame(window)
frame.pack()

#label
olabel = ttk.Label(frame, text="but blue:", style="Custom.TLabel")
olabel.pack(side="left", pady=5)
label = ttk.Label(frame, textvariable=int_var, style="Custom.TLabel")
label.pack(side="left",pady=5)



#run
window.mainloop()