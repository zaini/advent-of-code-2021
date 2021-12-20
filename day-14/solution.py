from collections import defaultdict


def apply_rules(template, pairs, n):
    print(n, len(template))
    if n == 0:
        return template

    inserts = {}

    for i in range(len(template) - 1):
        a = template[i]
        b = template[i + 1]

        x = a + b

        if x in pairs:
            inserts[i + 1] = pairs[x]

    res = ""
    for i in range(len(template)):
        if i in inserts:
            res += inserts[i]
        res += template[i]

    return apply_rules(res, pairs, n - 1)


def occurances(x):
    counts = defaultdict(int)
    for c in x:
        counts[c] += 1

    l, m = float("inf"), 0
    for count in counts:
        l = min(l, counts[count])
        m = max(m, counts[count])

    return l, m


def solution(template, pairs, n):
    """Question 1"""
    polymer = apply_rules(template, pairs, n)
    l, m = occurances(polymer)
    return m - l


def solution2(template, pairs, n):
    """Question 2"""
    return solution(template, pairs, n)


def parse_input():
    f = open("input.txt", "r").read().split("\n")
    template = f[0]
    pairs = {}
    for line in f[2:]:
        a, b = line.split(" -> ")
        pairs[a] = b
    return template, pairs


if __name__ == "__main__":
    template, pairs = parse_input()

    print("Question 1 solution: \n", solution(template, pairs, 10))
    print("Question 2 solution: \n", solution2(template, pairs, 40))
