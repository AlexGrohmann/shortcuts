import json

with open("shortcuts.json", "r") as file:
    data = json.load(file)

input = input("insert shortcut\n")
for shortcut in data["shortcuts"]:
    for key in shortcut["type"]:
        if key == input:
            print("Windows: " + shortcut["windows"])
            print("Mac: " + shortcut["mac"])
