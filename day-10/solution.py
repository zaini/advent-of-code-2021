PAIR = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}


def get_incomplete_stack(x):
    S = []
    for c in x:
        if S and c in PAIR and S[-1] == PAIR[c]:
            S.pop()
        else:
            S.append(c)
    return S


def first_invalid_character(x):
    S = []

    for c in x:
        if not S:
            S.append(c)
        else:
            if c in PAIR:
                if S[-1] != PAIR[c]:
                    return c
                else:
                    S.pop()
            else:
                S.append(c)
    return None


def is_corrupt(line):
    """Don't really needs this since first_invalid_character returns None/truthy"""
    if first_invalid_character(line):
        return True
    return False


def solution(lines):
    """Question 1"""
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
        None: 0
    }
    res = 0
    for line in lines:
        res += points[first_invalid_character(line)]
    return res


def solution2(lines):
    """
    Question 2
    This solution is ugly, just wanted it done though.
    """
    incomplete_lines = filter(lambda line: not is_corrupt(line), lines)
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
        None: 0
    }
    p = {PAIR[k]: k for k in PAIR}
    scores = []
    for line in incomplete_lines:
        S = get_incomplete_stack(line)
        score = 0
        for x in S[::-1]:
            score = (score * 5) + points[p[x]]
        scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


def parse_input():
    f = open("input.txt", "r").read().split("\n")
    res = []
    for line in f:
        res.append(line)
    return res


if __name__ == "__main__":
    lines = parse_input()

    print("Question 1 solution: \n", solution(lines))

    print("Question 2 solution: \n", solution2(lines))
