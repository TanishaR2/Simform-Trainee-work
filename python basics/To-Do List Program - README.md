This is a simple To-Do List program in Python with options to add, view, delete, and clear tasks. The tasks are saved in a text file (tasks.txt), and the program provides a menu-driven interface.
Concepts Used:

    Functions: Defined various functions for handling tasks like add_task, view_task, delete_task, etc.
    Decorators: Used show_list_before_after to display the task list before and after performing an operation.
    File Handling: Used to read from and write to a file (tasks.txt) to store the task list.
    Exception Handling: Used try-except to handle errors when deleting tasks or reading from the file.
    Lists: Stored tasks in a list (task_list) and manipulated them (add, delete, clear).

How it works:

    The user can choose from a menu to add, view, delete, or clear tasks.
    Tasks are read from tasks.txt when the program starts and saved back when the program ends.
    A decorator is used to show the task list before and after each operation.

Run the program and follow the on-screen menu to manage tasks.
