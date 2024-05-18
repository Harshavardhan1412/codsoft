import tkinter as tk
from tkinter import messagebox
def Add():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def Delete():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def Done():
    try:
        task_index = listbox.curselection()[0]
        listbox.itemconfig(task_index, {'bg':'yellow'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

def Clear():
    listbox.delete(0, tk.END)
root = tk.Tk()
root.title("To-Do List")
frame= tk.Frame(root)
frame.pack()

listbox= tk.Listbox(frame, height=15, width=45, bg="pink")
listbox.pack(side=tk.LEFT)

scrollbar= tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry= tk.Entry(root, width=50)
entry.pack()

button_add_task= tk.Button(root, text="Add Task", width=50, command=Add)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=50, command=Delete)
button_delete_task.pack()

button_mark_done = tk.Button(root, text="Mark Done", width=50, command=Done)
button_mark_done.pack()

button_clear_list = tk.Button(root, text="Clear List", width=48, command=Clear)
button_clear_list.pack()

root.mainloop()
