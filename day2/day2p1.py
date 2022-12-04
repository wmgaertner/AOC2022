import sys

file = open(sys.argv[1])

# Rock -> Paper -> Scissor
column_one = {"A": 1, "B": 2, "C": 3}
column_two = {"X": 1, "Y": 2, "Z": 3}


def play_game(input1, input2):
    result = column_one.get(input1) - column_two.get(input2)
    score = column_two.get(input2)
    if result == -1 or result == 2:
        # win
        score += 6
    elif result == 0:
        # draw
        score += 3
    else:
        # lose
        pass
    return score


total_score = 0
for line in file:
    line = line.strip()
    input1, input2 = line.split(sep=" ")
    total_score += play_game(input1, input2)
print(total_score)
