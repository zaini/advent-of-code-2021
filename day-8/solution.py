from collections import defaultdict


def count_chars(S):
    x = defaultdict(int)
    for c in S:
        x[c] += 1
    return x


digit_segments = {
    0: "abcefg", 1: "cf", 2: "acdeg", 3: "acdfg", 4: "bcdf",
    5: "abdfg", 6: "abdefg", 7: "acf", 8: "abcdefg", 9: "abcdfg"
}

correct = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
           "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
correct_count = count_chars("".join(correct))


def solution(signals):
    """Question 1"""
    res = 0
    for signal in signals:
        for word in signal[1]:
            if len(word) == 2:
                res += 1
            elif len(word) == 4:
                res += 1
            elif len(word) == 3:
                res += 1
            elif len(word) == 7:
                res += 1

    return res


def solution2(signals):
    """Question 2"""
    res = 0
    for signal in signals:
        # print(signal)
        # pairings = {}
        # for word in signal[0]:
        #     if len(word) == 2:
        #         pairings[1] = word
        #     elif len(word) == 4:
        #         pairings[4] = word
        #     elif len(word) == 3:
        #         pairings[7] = word
        #     elif len(word) == 7:
        #         pairings[8] = word

        num_pairings = {}
        for word in signal[0]:
            if len(word) == 2:
                num_pairings[1] = word
                res += 1
            elif len(word) == 4:
                num_pairings[4] = word
                res += 1
            elif len(word) == 3:
                num_pairings[7] = word
                res += 1
            elif len(word) == 7:
                num_pairings[8] = word
                res += 1

        # print(count_chars("".join(signal[0])))
        char_pairings = defaultdict(list)
        x = count_chars("".join(signal[0]))
        for key in x:
            if x[key] == 6:
                char_pairings["b"].append(key)
            elif x[key] == 4:
                char_pairings["e"].append(key)
            elif x[key] == 7:
                char_pairings["g"].append(key)
                char_pairings["d"].append(key)
            elif x[key] == 8:
                char_pairings["c"].append(key)
                char_pairings["a"].append(key)
            elif x[key] == 9:
                char_pairings["f"].append(key)
        print(char_pairings)
        print(num_pairings)
        print(correct_count)

    return res


def parse_input():
    f = open("input.txt", "r").read().split("\n")
    res = []
    for line in f:
        a, b = line.split(" | ")
        res.append((a.split(), b.split()))
    return res


if __name__ == "__main__":
    signals = parse_input()
    print(correct_count)

    print("Question 1 solution: \n", solution(signals))

    print("Question 2 solution: \n", solution2(signals))
