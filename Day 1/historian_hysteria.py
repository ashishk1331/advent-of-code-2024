from collections import Counter
from rich import print


# PART 1: just sort the lists
def part_one(inp):
    left = list(sorted(map(lambda x: x[0], inp)))
    right = list(sorted(map(lambda x: x[1], inp)))

    return sum([abs(left[index] - right[index]) for index in range(len(left))])


# PART 2: simple map op
def part_two(inp):
    left = map(lambda x: x[0], inp)
    right = Counter(map(lambda x: x[1], inp))

    score = 0
    for num in left:
        score += num * right.get(num, 0)

    return score


def main():
    input = []

    with open("input.txt", "r") as file:
        input = list(map(lambda x: tuple(map(int, x.split())), file.read().split("\n")))

    # print(part_one(input))
    print(part_two(input))


if __name__ == "__main__":
    main()
