import sys

file = open(sys.argv[1])

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

lines = file.read().splitlines()
i = 0
total_sum = 0
while i < len(lines):
    for char in lines[i]:
        if char in lines[i + 1]:
            if char in lines[i + 2]:
                total_sum += alphabet.find(char) + 1
                break
    i += 3
print(total_sum)
