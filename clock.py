import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # Update time every 1000 milliseconds (1 second)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('mono', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='ne')

time()
root.mainloop()