# PART 1:
def part_one(towels, patterns):

    def backtrack(pattern):

        if len(pattern) == 0:
            return True

        res = False

        for towel in towels:
            if pattern.startswith(towel):
                res = res or backtrack(pattern[len(towel) :])

        return res

    possible = 0

    for pattern in patterns:
        if backtrack(pattern):
            possible += 1

    return possible


# PART 2:
def part_two(towels, patterns):
    memo = {}

    def backtrack(pattern):

        if len(pattern) == 0:
            return True

        if pattern in memo:
            return memo[pattern]

        res = 0

        for towel in towels:
            if pattern.startswith(towel):
                res += backtrack(pattern[len(towel) :])

        memo[pattern] = res
        return res

    possible = 0

    for pattern in patterns:
        possible += backtrack(pattern)

    return possible


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")

        towels = list(map(str.strip, data.pop(0).split(",")))

        data.pop(0)

        patterns = data

    # print("Part 1:", part_one(towels, patterns))
    print("Part 2:", part_two(towels, patterns))


if __name__ == "__main__":
    main()
