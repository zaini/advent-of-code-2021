def step(octos):
    # gain energy
    for i in range(len(octos)):
        for j in range(len(octos[0])):
            octos[i][j][0] += 1

    # flashes
    flashes = True
    res = 0
    while flashes:
        flashes = False
        for i in range(len(octos)):
            for j in range(len(octos[0])):
                # an octo can only flash once per step
                if octos[i][j][0] > 9 and not octos[i][j][1]:
                    octos[i][j][1] = True
                    flashes = True
                    res += 1
                    # do += 1 for all diagonal octos
                    for x, y in [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]:
                        x += i
                        y += j
                        if x >= 0 and x < len(octos) and y >= 0 and y < len(octos[0]):
                            octos[x][y][0] += 1

    # all flashes octos have 0 energy
    for i in range(len(octos)):
        for j in range(len(octos[0])):
            if octos[i][j][1]:
                octos[i][j] = [0, False]

    return res


def display(octos):
    for line in octos:
        print("".join([str(x[0]) for x in line]))


def solution(octos):
    """Question 1"""
    return sum(step(octos) for _ in range(100))


def solution2(octos):
    """Question 2"""
    i = 0
    while True:
        # print(i)
        # display(octos)
        if sum([sum([x[0] for x in row]) for row in octos]) == 0:
            # Not fully sure why I need to do 100 + i, probably related to the board size
            return 100 + i
        i += 1
        step(octos)


def parse_input():
    f = open("input.txt", "r").read().split("\n")
    res = []
    for line in f:
        res.append([[int(x), False] for x in line])
    return res


if __name__ == "__main__":
    octos = parse_input()

    print("Question 1 solution: \n", solution(octos))

    print("Question 2 solution: \n", solution2(octos))
