import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Tk Text")
window.geometry("400x400")

#text
text = tk.Text(window,undo=True,maxundo=100,spacing1=10,spacing2=2,spacing3=5,height=5,wrap="char")
text.pack()

#run
window.mainloop()