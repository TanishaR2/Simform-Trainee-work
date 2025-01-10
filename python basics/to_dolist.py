def show_menu():
    print("To Do List Menu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Clear list")
    print("5. Exit")
    
def add_task(task_list):
    task = input("Enter the task: ")
    if task not in task_list:
        task_list.append(task)
        print(f"{task} added!")

    else:
        print("task already exist!")

def load_tasks():
    try:
        with open("tasks.txt", 'r') as file:
            return [task.strip() for task in file.readlines()]

    except FileNotFoundError:
        return []

def clear_list(task_list):
    task_list.clear()

def view_task(task_list):
    if task_list:
        print("Your To Do List: ")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")

    else:
        print("No tasks available")

def delete_task(task_list):
    if task_list:
        view_task(task_list)
        
        
        try:
            task = int(input("Enter the number of the task to be deleted: ")) - 1
            task_list.pop(task)

        except Exception as e:
            print(f"The list contains only {len(task_list)} elements")

    else:
        print("The list is empty you cant delete anything")


def save_task(task_list):
    with open("tasks.txt", 'w') as file:
        for task in task_list:
            file.write(task + "\n")

def main():
    
    task_list = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option(1,2,3,4): ")

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

        else:
            print("Please choose a valid option.")

        print("-------------------------------------------------")

           

if __name__ == '__main__':
    main()