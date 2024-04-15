import json

with open("shortcuts.json", "r") as file:
    data = json.load(file)


def favourites():
    for shortcut in data["shortcuts"]:
        try:
            if shortcut["favourite"]:

                for key in shortcut["type"]:
                    print(key.center(40, "#"))

                print("\nWindows: " + shortcut["windows"])
                print("Mac:     " + shortcut["mac"] + "\n")
                print("#".center(40, "#") + "\n")
        except KeyError:
            continue


def interact():
    user_input = input("insert shortcut\n")
    # exit
    if user_input == "exit":
        exit()

    if user_input == "":
        favourites()

    else:
        for shortcut in data["shortcuts"]:
            for key in shortcut["type"]:
                if user_input.lower() in str(key).lower():
                    print(key.center(40, "#"))
                    print("\nWindows: " + shortcut["windows"])
                    print("Mac:     " + shortcut["mac"] + "\n")
                    print("#".center(40, "#") + "\n")
    interact()


if __name__ == "__main__":
    interact()
