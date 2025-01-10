def show_menu():
    print("To Do List Menu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Clear list")
    print("5. Exit")

# Decorator to display task list before and after an operation
def show_list_before_after(func):
    def wrapper(task_list):
        print("Current To-Do List: ")
        view_task(task_list)  # Show the list before operation
        print("-------------------------------------------------")
        func(task_list)  # Perform the actual operation
        print("Updated To-Do List: ")
        view_task(task_list)  # Show the list after operation
        print("-------------------------------------------------")
    return wrapper

@show_list_before_after
def add_task(task_list):
    task = input("Enter the task: ")
    if task not in task_list:
        task_list.append(task)
        print(f"{task} added!")
    else:
        print("Task already exists!")

@show_list_before_after
def delete_task(task_list):
    if task_list:
        try:
            task = int(input("Enter the number of the task to be deleted: ")) - 1
            task_list.pop(task)
            print("Task deleted!")
        except Exception as e:
            print(f"The list contains only {len(task_list)} elements.")
    else:
        print("The list is empty, you can't delete anything.")

@show_list_before_after
def clear_list(task_list):
    task_list.clear()
    print("All tasks cleared!")

def load_tasks():
    try:
        with open("tasks.txt", 'r') as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_task(task_list):
    with open("tasks.txt", 'w') as file:
        for task in task_list:
            file.write(task + "\n")

def view_task(task_list):
    if task_list:
        print("Your To-Do List: ")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available")

def main():
    task_list = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1,2,3,4,5): ")

        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_task(task_list)
        elif choice == '3':
            delete_task(task_list)
        elif choice == '4':
            clear_list(task_list)
        elif choice == '5':
            save_task(task_list)
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option.")
        print("-------------------------------------------------")

if __name__ == '__main__':
    main()
