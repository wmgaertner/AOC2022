import sys

file = open(sys.argv[1])


calories_list = []
calories = 0
for line in file:
    if line.strip().isdigit():
        calories += int(line)
    if line.isspace():
        calories_list.append(calories)
        calories = 0
# in case file doesn't end on empty line
if calories != 0:
    calories_list.append(calories)

calories_list.sort(reverse=True)
total_calories = calories_list[0] + calories_list[1] + calories_list[2]

print(total_calories)
