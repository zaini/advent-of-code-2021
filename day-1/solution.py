def measurements_larger_than_previous(lst):
    lst.insert(0, float("inf"))
    res = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            res += 1
    return res

def convert_to_sliding_window_sums(lst, size):
    if len(lst) < size:
        print("Size must less than or equal to the length of the list")
        return
    
    cur = 0
    for i in range(size):
        cur += lst[i]
    
    i = 0
    j = size - 1

    res = [cur]

    for j in range(size, len(lst)):
        cur -= lst[i]
        i += 1
        cur += lst[j]
        res.append(cur)

    return res

def parse_input():
    f = open("input.txt", "r")
    lst = []
    for line in f:
        lst.append(int(line))
    return lst

if __name__ == "__main__":
    x = parse_input()
    print("Question 1 solution: \n", measurements_larger_than_previous(x))

    x = parse_input()
    print("Question 2 solution: \n", measurements_larger_than_previous(convert_to_sliding_window_sums(x, 3)))
