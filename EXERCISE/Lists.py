import tkinter as tk

def table():
    num = int(entry.get())
    result = ""
    for i in range(1, 13):
        result += f"{num} x {i} = {num * i}\n"
    output.set(result)

#window
window = tk.Tk()
window.title("Times Table")
window.geometry("300x400")

#input
entry = tk.Entry(window)
entry.pack(pady=10)

#button
button = tk.Button(window, text="Show Table", command=table)
button.pack(pady=10)

#label
output = tk.StringVar()
label = tk.Label(window, textvariable=output, justify="left")
label.pack(pady=10)

#run
window.mainloop()
