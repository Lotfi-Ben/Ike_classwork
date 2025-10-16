import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def options():
    choice = int_var.get()
    if choice == 1:
        showinfo(title='Choice', message="two")
    elif choice == 2:
        showinfo(title='Choice', message="three")

#window
window = tk.Tk()
window.title("Radio Button")
window.geometry("400x400")

#frame
frame = ttk.Frame(window)

#radiobuttons
int_var = tk.IntVar()
Int_radiobutton_1 = ttk.Radiobutton(frame, value=1, variable=int_var, text='This is One')
Int_radiobutton_2 = ttk.Radiobutton(frame, value=2, variable=int_var, text='This is Two')
Int_radiobutton_1.pack()
Int_radiobutton_2.pack()
frame.pack()

#button
check_button = ttk.Button(window, text="Choose", command=options)
check_button.pack(pady=10)

#run
window.mainloop()
