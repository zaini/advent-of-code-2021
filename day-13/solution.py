from collections import defaultdict


def get_size(dots):
    h, w = 0, 0
    for x, y in dots:
        h = max(h, y)
        w = max(w, x)
    return h, w


def display(board):
    for row in board:
        print("".join("#" if x == 1 else "." for x in row))


def fold(board, dir, pos):
    if dir == "y":
        for i in range(pos, len(board)):
            row = board[i]
            for j in range(len(row)):
                if row[j]:
                    # print((i, j), (pos + pos - i, j))
                    board[pos + pos - i][j] = 1
        return board[:pos]
    elif dir == "x":
        for i in range(len(board)):
            row = board[i]
            for j in range(pos, len(row)):
                if row[j]:
                    board[i][pos + pos - j] = 1
        return [row[:pos] for row in board]


def solution(dots, folds):
    """Question 1"""
    h, w = get_size(dots)
    board = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    for x, y in dots:
        board[y][x] = 1

    dir, pos = folds[0]
    board = fold(board, dir, pos)

    return sum(sum(row) for row in board)


def solution2(dots, folds):
    """Question 2"""
    h, w = get_size(dots)
    board = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    for x, y in dots:
        board[y][x] = 1

    for f in folds:
        dir, pos = f
        board = fold(board, dir, pos)

    return board


def parse_input():
    dots = []
    folds = []

    f = open("input.txt", "r")

    line = f.readline().strip()

    while line:
        x, y = line.split(",")
        dots.append((int(x), int(y)))
        line = f.readline().strip()

    line = f.readline().strip()

    while line:
        _, __, instruction = line.split()
        a, b = instruction.split("=")
        folds.append((a, int(b)))
        line = f.readline().strip()

    return dots, folds


if __name__ == "__main__":
    dots, folds = parse_input()

    print("Question 1 solution: \n", solution(dots, folds))

    board = solution2(dots, folds)
    print("Question 2 solution: \n")
    display(board)
