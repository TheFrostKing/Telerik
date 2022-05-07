commands = input()
x_dict = {
    'R' : 1,
    'L' : -1
}

y_dict = {
    'U': 1,
    'D': -1
}

y = 0
x = 0

for command in commands:
    if command in y_dict:
        y += y_dict[command]

    if command in x_dict:
        x += x_dict[command]


print(f"({x}, {y})")
