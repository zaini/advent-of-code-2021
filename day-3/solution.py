from collections import defaultdict

def binary_array_to_decimal(lst):
    res = 0
    base = 2
    j = 0
    lst = lst[::-1]
    for i in range(len(lst)):
        res += int(lst[i]) * (base ** i)
    return res

# Question 1
def get_power_consumption(lst):
    counts = defaultdict(lambda: [0, 0])

    for x in lst:
        for i, b in enumerate(x):
            if b == '1':
                counts[i][1] += 1
            elif b == '0':
                counts[i][0] += 1

    most_common = [1 if counts[x][1] > counts[x][0] else 0 for x in counts]
    least_common = [1 if counts[x][1] < counts[x][0] else 0 for x in counts]

    gamma_rate = binary_array_to_decimal(most_common)
    epsilon_rate = binary_array_to_decimal(least_common)

    return gamma_rate * epsilon_rate

# Question 2
def get_life_support_rating(lst):
    # find oxygen generator rating
    valid = lst
    i = 0
    while len(valid) > 1:
        verified = []

        counts = [0, 0]

        for x in valid:
            if x[i] == '1':
                counts[1] += 1
            elif x[i] == '0':
                counts[0] += 1

        most_common = 1 if counts[1] >= counts[0] else 0
        # least_common = 1 if counts[x][1] < counts[x][0] else 0

        for x in valid:
            if most_common == int(x[i]):
                verified.append(x)
        valid = verified
        i += 1

    a = binary_array_to_decimal(valid[0])

    # find C02 scrubber rating
    valid = lst
    i = 0
    while len(valid) > 1:
        verified = []

        counts = [0, 0]

        for x in valid:
            if x[i] == '1':
                counts[1] += 1
            elif x[i] == '0':
                counts[0] += 1

        least_common = 1 if counts[1] < counts[0] else 0

        for x in valid:
            if least_common == int(x[i]):
                verified.append(x)
        valid = verified
        i += 1

    b = binary_array_to_decimal(valid[0])

    return a * b

def parse_input():
    f = open("input.txt", "r").read().split("\n")
    return f

if __name__ == "__main__":
    x = parse_input()
    print("Question 1 solution: \n", get_power_consumption(x))

    print("Question 2 solution: \n", get_life_support_rating(x))
