class Fish:
    def __init__(self, age: int = 8) -> None:
        self.age = age

    def live_day(self):
        """Live a day and return a fish if it's now old enough to produce a fish"""
        if self.age < 7:
            self.age = (self.age - 1) % 7
            if self.age == 6:
                return Fish()
        else:
            self.age -= 1
        return None

    def __str__(self) -> str:
        return str(self.age)


def solution(fishes, days=80):
    """Question 1"""
    for day in range(days):
        # print(day, [str(fish) for fish in fishes])
        # print(day, len(fishes))
        for i in range(len(fishes)):
            fish = fishes[i]
            res = fish.live_day()
            if res:
                fishes.append(res)

    return len(fishes)


def solution2(fishes, days=256):
    fishes = [fish.age for fish in fishes]
    fishes = [fishes.count(age) for age in range(9)]
    for _ in range(days):
        # [0 age fishes, 1 age fishes, ..., 8 age fishes]
        # after 1 day, there will be len(0 age fishes) new fishes, so we add them to the end as the new 8 age fishes
        # we then move all the other fishes down one
        born_fishes = fishes.pop(0)
        fishes[6] += born_fishes
        fishes.append(born_fishes)
    return sum(fishes)


def parse_input():
    return [Fish(int(x)) for x in open("input.txt", "r").read().split(",")]


if __name__ == "__main__":
    fishes = parse_input()
    print("Question 1 solution: \n", solution(fishes))
    fishes = parse_input()
    print("Question 2 solution: \n", solution2(fishes))

    # res = 0
    # for age in [3, 4, 3, 1, 2]:
    #     x = f(age, 80)
    #     res += x
    #     print(age, x)
    # print(res)

    # key: (age, days), value: fishes produced at the end
    # helper = {}
    # for age in range(9):
    #     for days in range(90):
    #         fishes = [Fish(age)]
    #         res = solution(fishes, days)
    #         # print(f"age: {age}, days: {days}, fishes produced: {res}")
    #         print(age, days, res)
    #     helper[(age, days)] = res
    # print(helper)
