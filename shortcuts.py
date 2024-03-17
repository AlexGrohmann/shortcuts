import json

with open("shortcuts.json", "r") as file:
    data = json.load(file)


def interact():
    user_input = input("insert shortcut\n")
    # exit
    if user_input == "exit":
        exit()

    for shortcut in data["shortcuts"]:
        for key in shortcut["type"]:
            if key == user_input:
                print(key.center(40, "#"))
                print("\nWindows: " + shortcut["windows"])
                print("Mac:     " + shortcut["mac"] + "\n")
                print("#".center(40, "#") + "\n")
        interact()


if __name__ == "__main__":
    interact()
