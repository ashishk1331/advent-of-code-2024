from collections import Counter
from rich import print


# PART 1:
def part_one(inp):
    safe = 0

    for report in inp:
        isSafe = True
        flag = report[1] - report[0]
        first = report[0]

        for index, value in enumerate(report[1:], 1):
            diff = value - report[index - 1]
            if flag > 0:
                if diff < 1 or diff > 3:
                    isSafe = False
                    break
            else:
                if (diff >= 0) or (abs(diff) < 1 or abs(diff) > 3):
                    isSafe = False
                    break

        if isSafe:
            safe += 1

    return safe


# PART 2:
def part_two(inp):
    safe = 0
    for report in inp:
        sample = []
        for index in range(len(report)):
            sample.append(report[:index] + report[index + 1 :])
        if part_one(sample) > 0:
            safe += 1
    return safe


def main():
    input = []

    with open("input.txt", "r") as file:
        input = list(map(lambda x: tuple(map(int, x.split())), file.read().split("\n")))

    print(part_one(input))
    print(part_two(input))


if __name__ == "__main__":
    main()
