FILEPATH = 'todos.txt'

# Function to read todos from the file
def read_todos():
    """
    Reads the list of todos from the FILEPATH file.

    Returns:
        list: A list of todos read from the file, or an empty list if the file does not exist.
    """
    try:
        with open(FILEPATH, 'r') as f:
            return f.readlines()  # Return the list of todos
    except FileNotFoundError:
        return []  # Return an empty list if file does not exist


# Function to write todos to the file
def write_todos(todos_local):
    """
    Writes the provided list of todos to the FILEPATH file.
    Args:
        todos_local (list): The list of todos to be written to the file.
    """
    with open(FILEPATH, 'w') as f:
        f.writelines(todos_local)  # Write the updated todos to the file


# Function to get todo number from user input
def get_todo_number(action, todos_local):
    """
    Retrieves and validates the todo number from the user input.

    Args:
        action (str): The user input containing the todo number.
        todos_local (list): The current list of todos.

    Returns:
        int: The index of the selected todo item (0-based index).

    Raises:
        ValueError: If the user input is not a valid number.
        IndexError: If the number is out of the valid range of todo items.
    """
    try:
        number_local = int(action.strip()) - 1
        if number_local < 0 or number_local >= len(todos_local):
            raise IndexError("Invalid todo number.")
        return number_local
    except ValueError:
        raise ValueError("Please enter a valid number.")
    except IndexError:
        raise IndexError("Invalid todo number. Please try again.")


# Function to confirm user actions (like delete)
def confirm_action(message):
    """
    Asks the user for confirmation before proceeding with a specific action.

    Args:
        message (str): The confirmation message to display to the user.

    Returns:
        bool: True if the user confirms with 'Yes', False otherwise.
    """
    answer = input(f"{message} (Yes/No): ").strip().capitalize()
    return answer == 'Yes'
