def solution(crabs):
    """Question 1"""
    """
    Find most common position, move all crabs to that position
    Find the average position and move all crabs to that
    -> Brute force calculation
    """
    res = float("inf")
    for final_pos in range(max(crabs)):
        total = 0
        for crab in crabs:
            total += abs(crab - final_pos)
        res = min(res, total)
    return res


def solution2(crabs):
    """Question 2"""
    res = float("inf")
    for final_pos in range(max(crabs)):
        total = 0
        for crab in crabs:
            moves = abs(crab - final_pos)
            total += moves * (moves + 1) // 2
        res = min(res, total)
    return res


def parse_input():
    return [int(x) for x in open("input.txt", "r").read().split(",")]


if __name__ == "__main__":
    # This is by far the easiest one so far it feels...
    crabs = parse_input()

    print("Question 1 solution: \n", solution(crabs))

    print("Question 2 solution: \n", solution2(crabs))
