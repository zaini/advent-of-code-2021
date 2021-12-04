import re

def score(board, draw):
    total = 0
    for row in board:
        for val, drawn in row:
            if not drawn:
                total += val
    return total * draw

# Question 1
def solution(draws, boards):
    for draw in draws:
        # apply the draw
        for i, board in enumerate(boards):
            # print(board)
            for j, row in enumerate(board):
                # print(j, row)
                for k, (val, drawn) in enumerate(row):
                    # print(k, val, drawn)
                    if val == draw:
                        # print(i, j, k)
                        boards[i][j][k][1] = True
        
        # check if we have a winner
            # if winner, calculate and return result
            # else continue
        for i, board in enumerate(boards):
            # print(board)
            # check rows
            for j, row in enumerate(board):
                # print(j, row)
                winner = True
                for k, (val, drawn) in enumerate(row):
                    winner = winner and drawn
                if winner:
                    return score(board, draw)

            # check cols
            # This could be wrong
            for col in range(len(board)):
                winner = True
                for row in range(len(board[0])):
                    val, drawn = board[row][col]
                    winner = winner and drawn
                if winner:
                    return score(board, draw)

# Question 2
def solution2(draws, boards):
    for draw in draws:
        # apply the draw
        for i, board in enumerate(boards):
            # print(board)
            for j, row in enumerate(board):
                # print(j, row)
                for k, (val, drawn) in enumerate(row):
                    # print(k, val, drawn)
                    if val == draw:
                        # print(i, j, k)
                        boards[i][j][k][1] = True
        
        winners = []
        # check if we have a winner
            # if winner, calculate and return result
            # else continue
        for i, board in enumerate(boards):
            # print(board)
            # check rows
            for j, row in enumerate(board):
                # print(j, row)
                winner = True
                for k, (val, drawn) in enumerate(row):
                    winner = winner and drawn
                if winner:
                    if len(boards) == 1:
                        return score(board, draw)
                    winners.append(board)

            # check cols
            # This could be wrong
            for col in range(len(board)):
                winner = True
                for row in range(len(board[0])):
                    val, drawn = board[row][col]
                    winner = winner and drawn
                if winner:
                    if len(boards) == 1:
                        return score(board, draw)
                    winners.append(board)

        for winner in winners:
            if winner in boards:
                boards.remove(winner)
            

def parse_input():
    f = open("input.txt", "r").read().split("\n")
    draws = [int(x) for x in f[0].split(",")]

    boards = []
    
    line = 2
    while line < len(f):
        board = []
        for i in range(line, line + 5):
            board.append([[int(x), False] for x in f[line].split()])
            line += 1
        line += 1
        boards.append(board)

    return (draws, boards)

if __name__ == "__main__":
    draws, boards = parse_input()
    print("Question 1 solution: \n", solution(draws, boards))

    print("Question 2 solution: \n", solution2(draws, boards))
