import tkinter as tk

win = tk.Tk()
win.title("To-Do List")
win.geometry("400x300")
win.config(bg="white")

heading = tk.Label(win, text="--- TO-DO LIST MENU ---", font=("Arial", 16, "bold"), bg="white", fg="darkblue")
heading.pack(pady=15)

add_btn = tk.Button(win, text="1. Add Task", font=("Arial", 12), width=20, bg="lightgreen")
add_btn.pack(pady=5)

view_btn = tk.Button(win, text="2. View Tasks", font=("Arial", 12), width=20, bg="skyblue")
view_btn.pack(pady=5)

remove_btn = tk.Button(win, text="3. Remove Task", font=("Arial", 12), width=20, bg="tomato")
remove_btn.pack(pady=5)

exit_btn = tk.Button(win, text="4. Exit", font=("Arial", 12), width=20, bg="orange", command=win.destroy)
exit_btn.pack(pady=5)

win.mainloop()

tasks = []

while True:
    print("\n TO-DO LIST MENU ")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"Task '{removed}' removed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting To-Do List!")
        break