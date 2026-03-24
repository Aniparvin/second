import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    try:
        selected_index = task_list.curselection()[0]
        task_list.delete(selected_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# ------------------ UI SETUP ------------------------
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

task_list = tk.Listbox(root, width=30, height=10)
task_list.pack(pady=10)

root.mainloop()


