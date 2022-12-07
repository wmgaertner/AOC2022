import sys

file = open(sys.argv[1]).readlines()


def part1():
    char_list = [*file[0][0:4]]
    count = 0
    unique = False
    while unique != True:
        if len(set(char_list)) == len(char_list):
            unique = True
        else:
            char_list.pop(0)
            char_list.append(file[0][4 + count])
            count += 1
    print(count + 4)


def part2():
    char_list = [*file[0][0:14]]
    count = 0
    unique = False
    while unique != True:
        if len(set(char_list)) == len(char_list):
            unique = True
        else:
            char_list.pop(0)
            char_list.append(file[0][14 + count])
            count += 1
    print(count + 14)


if __name__ == "__main__":
    part1()
    part2()
