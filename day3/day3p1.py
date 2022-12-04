import sys
file = open(sys.argv[1])

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total_sum = 0
for line in file:
    line = line.strip()
    length = len(line)
    line1 = line[:length//2]
    line2 = line[length//2:]
    for char in line1:
        if char in line2:
            total_sum += alphabet.find(char)+1
            break
print(total_sum)
