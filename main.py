import time
from functions import *

now = time.strftime("%B %d, %Y %H:%M:%S")
print("It is", now)
# Main loop to handle user commands
while True:
    try:
        user_action = input("Type add, show, edit, complete, delete, or exit: ").strip().lower()

        if user_action.startswith("add"):
            """
            Handles the 'add' command by adding a new todo item.
            """
            todo = user_action[4:].capitalize().strip()
            if not todo:
                raise ValueError("You must enter a todo item.")
            todos = read_todos()  # Read existing todos
            todos.append(todo + "\n")  # Add the new todo
            write_todos(todos)  # Save updated todos

        elif user_action.startswith("show"):
            """
            Handles the 'show' command by displaying all the existing todos.
            """
            todos = read_todos()
            if not todos:
                print("There are no todos to show.")
            else:
                for index, todo in enumerate(todos):
                    print(f"{index + 1} - {todo.strip()}")

        elif user_action.startswith("edit"):
            """
            Handles the 'edit' command by allowing the user to edit a specific todo item.
            """
            todos = read_todos()
            if not todos:
                print("No todos available for editing.")
                continue
            try:
                number = get_todo_number(user_action[4:], todos)
                print(f"Current todo: {todos[number].strip()}")
                new_todo = input("Enter a new todo: ").capitalize().strip()
                if not new_todo:
                    raise ValueError("You must enter a new todo item.")
                todos[number] = new_todo + "\n"  # Update the selected todo
                write_todos(todos)
            except (ValueError, IndexError) as e:
                print(e)

        elif user_action.startswith("complete"):
            """
            Handles the 'complete' command by marking a specific todo item as completed.
            """
            todos = read_todos()
            if not todos:
                print("No todos available to complete.")
                continue
            try:
                number = get_todo_number(user_action[8:], todos)
                completed_todo = todos.pop(number).strip()
                write_todos(todos)
                print(f"Todo '{completed_todo}' has been completed.")
            except (ValueError, IndexError) as e:
                print(e)

        elif user_action.startswith("delete"):
            """
            Handles the 'delete' command by allowing the user to delete a specific todo item.
            """
            todos = read_todos()
            if not todos:
                print("No todos available to delete.")
                continue
            try:
                number = get_todo_number(user_action[6:], todos)
                todo_to_delete = todos[number].strip()
                if confirm_action(f"Are you sure you want to delete '{todo_to_delete}'?"):
                    todos.pop(number)  # Remove the selected todo
                    write_todos(todos)
                    print(f"Todo '{todo_to_delete}' has been deleted.")
                else:
                    print("Delete operation cancelled.")
            except (ValueError, IndexError) as e:
                print(e)

        elif user_action == "exit":
            """
            Exits the todo application.
            """
            print("Bye...")
            break

        else:
            print("Invalid command. Please try again.")

    except ValueError as e:
        print(e)
