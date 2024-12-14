# PART 1:
def part_one(inp):
    mus = 0

    def backtrack(seq, total):
        if len(seq) == 1:
            return seq[0] == total

        res = False
        a, b = seq[:2]
        seq = seq[2:]

        # addition operation
        seq.insert(0, a + b)
        res = res or backtrack(seq, total)

        seq = seq[1:]
        # multiply operation
        seq.insert(0, a * b)
        res = res or backtrack(seq, total)

        return res

    for total, seq in inp:
        if backtrack(seq, total):
            mus += total

    return mus


# PART 2:
def part_two(inp):
    return inp


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")
        seq = []
        for each in data:
            total, nums = list(map(str.strip, each.split(":")))
            total = int(total)
            nums = list(map(int, nums.split()))
            seq.append((total, nums))
        data = seq

    # print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
