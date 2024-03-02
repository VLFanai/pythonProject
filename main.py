import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

root = tk.Tk()
root.title("Notes App")
root.geometry("500x500")
style = Style(theme='journal')
style = ttk.Style()

#Configurate the tab font to be bold
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

notebook = ttk.Notebook(root, style="TNotebook")

notes = {}
try:
    with open("otes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    pass

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

def add_note():
