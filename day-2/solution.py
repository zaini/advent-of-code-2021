# Question 1
def displacement(commands):
    start = [0, 0]

    for direction, distance in commands:
        if direction == "forward":
            start[0] += distance
        elif direction == "up":
            start[1] -= distance
        elif direction == "down":
            start[1] += distance

    return start[0] * start[1]

# Question 2
def aim(commands):
    start = [0, 0]
    aim = 0

    for direction, distance in commands:
        if direction == "forward":
            start[0] += distance
            start[1] += aim * distance
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance

    return start[0] * start[1]

def parse_input():
    f = open("input.txt", "r").read().split("\n")
    lst = []
    for line in f:
        direction, distance = line.split(" ")
        lst.append((direction, int(distance)))
    return lst

if __name__ == "__main__":
    commands = parse_input()
    print("Question 1 solution: \n", displacement(commands))

    print("Question 2 solution: \n", aim(commands))
