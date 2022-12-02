file = open("input.txt")

calories = 0
max_calories = 0
for line in file:
    if (line.strip().isdigit()):
        calories += int(line)
    if (line.isspace()):
        if calories > max_calories:
            max_calories = calories
        calories = 0
# in case file doesn't end on empty line
if (calories != 0):
    if calories > max_calories:
            max_calories = calories
print("Most calories = ")
print(max_calories)