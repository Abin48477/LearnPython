todos = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        task = input("Enter task: ")
        todos.append({"task": task, "done": False})
        print("Task added!")
    
    elif choice == "2":
        if not todos:
            print("No tasks!")
        else:
            for i, item in enumerate(todos, 1):
                status = "✓" if item["done"] else "✗"
                print(f"{i}. [{status}] {item['task']}")
    
    elif choice == "3":
        try:
            num = int(input("Task number to mark done: ")) - 1
            todos[num]["done"] = True
            print("Task marked as done!")
        except:
            print("Invalid task number!")
    
    elif choice == "4":
        try:
            num = int(input("Task number to delete: ")) - 1
            del todos[num]
            print("Task deleted!")
        except:
            print("Invalid task number!")
    
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")