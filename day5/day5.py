import sys

file = open(sys.argv[1]).readlines()


def part1():
    def move_crates(amount: int, source: int, destination: int):
        for i in range(amount):

            supply_crates[destination - 1].append(supply_crates[source - 1].pop())

    # Get number of stacks and init empty 2d list to contain crates
    stacks_count = len(file[0].replace("/n", "")) // 4

    supply_crates = [[] for i in range(stacks_count)]

    for line in file:
        line = line.rstrip()
        i = 0
        # read data into stacks
        for char in line:
            if char == "[":
                stackNum = i // 4
                supply_crates[stackNum].insert(0, line[i + 1])
            elif char == "1":
                break
            i += 1

        # move crates between stacks
        if line.startswith("move"):

            order = line.split(" ")
            move_crates(int(order[1]), int(order[3]), int(order[5]))

    message = ""
    for stack in supply_crates:
        message += stack[-1]
    print("Part 1 solution: ", message)


def part2():
    def move_crates(amount: int, source: int, destination: int):

        temp_crates = supply_crates[source - 1][-amount:]
        for crate in temp_crates:
            supply_crates[destination - 1].append(crate)
            supply_crates[source - 1].pop()

    # Get number of stacks and init empty 2d list to contain crates
    stacks_count = len(file[0].replace("/n", "")) // 4

    supply_crates = [[] for i in range(stacks_count)]

    for line in file:
        line = line.rstrip()
        i = 0
        # read data into stacks
        for char in line:
            if char == "[":
                stackNum = i // 4
                supply_crates[stackNum].insert(0, line[i + 1])
            elif char == "1":
                break
            i += 1

        # move crates between stacks
        if line.startswith("move"):

            order = line.split(" ")
            move_crates(int(order[1]), int(order[3]), int(order[5]))

    message = ""
    for stack in supply_crates:
        message += stack[-1]
    print("Part 2 solution: ", message)


if __name__ == "__main__":
    part1()
    part2()
