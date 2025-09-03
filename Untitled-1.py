import tkinter as tk
from tkinter import messagebox, simpledialog

tasks = []

def add_task():
    task = simpledialog.askstring("Add Task", "Enter task:")
    if task:
        tasks.append(task)
        messagebox.showinfo("Task Added", f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        messagebox.showinfo("Tasks", "No tasks yet.")
    else:
        task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        messagebox.showinfo("Your Tasks", task_list)

def remove_task():
    if not tasks:
        messagebox.showwarning("Warning", "No tasks to remove.")
    else:
        task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        try:
            index = simpledialog.askinteger("Remove Task", f"Your Tasks:\n{task_list}\n\nEnter task number to remove:")
            if index is None:
                return
            index -= 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                messagebox.showinfo("Removed", f"Task '{removed}' removed!")
            else:
                messagebox.showwarning("Warning", "Invalid task number.")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number.")

def exit_app():
    messagebox.showinfo("Exit", "Exiting To-Do List!")
    win.destroy()

win = tk.Tk()
win.title("To-Do List")
win.geometry("400x300")
win.config(bg="white")

heading = tk.Label(win, text="--- TO-DO LIST MENU ---", font=("Arial", 16, "bold"), bg="white", fg="darkblue")
heading.pack(pady=15)

add_btn = tk.Button(win, text="1. Add Task", font=("Arial", 12), width=20, bg="lightgreen", command=add_task)
add_btn.pack(pady=5)

view_btn = tk.Button(win, text="2. View Tasks", font=("Arial", 12), width=20, bg="skyblue", command=view_tasks)
view_btn.pack(pady=5)

remove_btn = tk.Button(win, text="3. Remove Task", font=("Arial", 12), width=20, bg="tomato", command=remove_task)
remove_btn.pack(pady=5)

exit_btn = tk.Button(win, text="4. Exit", font=("Arial", 12), width=20, bg="orange", command=exit_app)
exit_btn.pack(pady=5)

win.mainloop()
