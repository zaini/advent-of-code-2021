def solution(transitions, height, width):
    """Question 1"""
    board = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for start, end in transitions:
        x1, y1 = start
        x2, y2 = end

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        # No diagonals
        if not (dy and dx):
            if not dy:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    board[y1][i] += 1
            elif not dx:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    board[i][x1] += 1

    # count how many values >=2
    res = 0
    for row in board:
        for val in row:
            if val >= 2:
                res += 1

    return res


def solution2(transitions, height, width):
    """Question 2"""
    board = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for start, end in transitions:
        x1, y1 = start
        x2, y2 = end

        dy = y2 - y1
        dx = x2 - x1

        if not (dy and dx):
            if not dy:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    board[y1][i] += 1
            elif not dx:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    board[i][x1] += 1
        else:
            while x1 != x2 and y1 != y2 and x1 < width and y1 < height and x1 >= 0 and y1 >= 0:
                board[y1][x1] += 1

                if dx < 0:
                    x1 -= 1
                else:
                    x1 += 1

                if dy < 0:
                    y1 -= 1
                else:
                    y1 += 1
            board[y2][x2] += 1

    # count how many values >=2
    res = 0
    for row in board:
        # print("".join([str(x) if x != 0 else "." for x in row]))
        for val in row:
            if val >= 2:
                res += 1

    return res


def parse_input():
    f = open("input.txt", "r").read().split("\n")
    height, width = 0, 0
    transitions = []
    for line in f:
        a, b = line.split(" -> ")
        x1, y1 = a.split(",")
        x2, y2 = b.split(",")
        height = max(height, int(y1), int(y2))
        width = max(width, int(x1), int(x2))
        transitions.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return transitions, height, width


if __name__ == "__main__":
    transitions, height, width = parse_input()
    print("Question 1 solution: \n", solution(transitions, height, width))

    print("Question 2 solution: \n", solution2(transitions, height, width))
