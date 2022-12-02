file = open("input.txt")

# Rock -> Paper -> Scissor 
column_one = {'A': 1, 'B': 2, 'C': 3}



def play_game(input1, input2):
    player1_input = column_one.get(input1)
    score = 0
    if (input2 == "X"):
        # lose
        if (player1_input > 1):
            score = player1_input - 1
        else:
            score = 3
    elif (input2 == "Y"):
        # draw
        score = player1_input + 3
    elif (input2 == "Z"):
        # win
        if (player1_input < 3):
            score = player1_input + 1
        else:
            score = 1
        score += 6    
    
    return score

total_score = 0
for line in file:
    line = line.strip()
    input1, input2 = line.split(sep=' ')
    total_score += play_game(input1, input2)
print(total_score)