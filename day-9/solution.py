def is_low_point(board, i, j):
    neighbours = []
    if i > 0:
        neighbours.append((i - 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if i < len(board) - 1:
        neighbours.append((i + 1, j))
    if j < len(board[0]) - 1:
        neighbours.append((i, j + 1))

    return all([board[i][j] < board[x][y] for x, y in neighbours])


def get_low_points(board):
    low_points = []

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if is_low_point(board, i, j):
                low_points.append((i, j))

    return low_points


def solution(board):
    """Question 1"""
    risk_score = 0
    for x, y in get_low_points(board):
        risk_score += 1 + board[x][y]

    return risk_score


def get_basin_size(board, i, j, flowing_into):
    size = 0
    if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] != -1 and board[i][j] >= flowing_into and board[i][j] != 9:
        flowing_into = board[i][j]
        board[i][j] = -1
        size += 1
        size += get_basin_size(board, i + 1, j, flowing_into)
        size += get_basin_size(board, i - 1, j, flowing_into)
        size += get_basin_size(board, i, j + 1, flowing_into)
        size += get_basin_size(board, i, j - 1, flowing_into)
    return size


def solution2(board):
    """Question 2"""
    low_points = set(get_low_points(board))
    basins = []  # stores the sizes of basins

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != -1 and (i, j) in low_points:
                x = get_basin_size(board, i, j, float("-inf"))
                basins.append(x)

    res = 1
    for basin_size in sorted(basins, reverse=True)[:3]:
        res *= basin_size
    return res


def parse_input():
    f = open("input.txt", "r").read().split("\n")
    board = []
    for line in f:
        row = []
        for c in line:
            row.append(int(c))
        board.append(row)
    return board


if __name__ == "__main__":
    board = parse_input()

    print("Question 1 solution: \n", solution(board))

    print("Question 2 solution: \n", solution2(board))
