# print("Hello I return shortcuts for Windows and Mac (incl. Visual Studio Code)")
# print("Input: copy")
# print("Output: Windows: strg + c, Mac: ??? + c")
import json

# Retrieve JSON data from the file
with open("shortcuts.json", "r") as file:
    data = json.load(file)

input = input("insert shortcut\n")
# Access and process the retrieved JSON data
for shortcut in data["shortcuts"]:
    for key in shortcut["type"]:
        if key == input:
            print("Windows: " + shortcut["windows"])
            print("Mac: " + shortcut["mac"])
