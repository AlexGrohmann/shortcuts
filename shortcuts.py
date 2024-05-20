import json
import sys


# Load data from the JSON file
def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' is not a valid JSON.")
        sys.exit(1)


# Print a single shortcut
def print_shortcut(shortcut):
    for key in shortcut["type"]:
        print(key.center(40, "#"))

    print("\nWindows: " + shortcut["windows"])
    print("Mac:     " + shortcut["mac"] + "\n")
    print("#".center(40, "#") + "\n")


# Print all favourite shortcuts
def print_favourites(data):
    for shortcut in data.get("shortcuts", []):
        if shortcut.get("favourite"):
            print_shortcut(shortcut)


# Interact with the user to find shortcuts
def interact(data):
    while True:
        user_input = input("Insert shortcut or 'exit' to quit:\n").strip().lower()

        if user_input == "exit":
            break

        if user_input == "":
            print_favourites(data)
        else:
            found = False
            for shortcut in data.get("shortcuts", []):
                if any(user_input in str(key).lower() for key in shortcut["type"]):
                    print_shortcut(shortcut)
                    found = True

            if not found:
                print("Shortcut not found. Please try again.")


# Main function
def main():
    data = load_data("shortcuts.json")
    interact(data)


if __name__ == "__main__":
    main()
