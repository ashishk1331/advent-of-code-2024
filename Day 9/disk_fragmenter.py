# PART 1:
def part_one(inp):
    n = len(inp)
    disk = []

    for ind in range(0, n, 2):
        file_size = int(inp[ind])
        empty_size = int(inp[ind + 1]) if ind + 1 < n else 0
        disk.extend([str(ind // 2)] * file_size + ["."] * empty_size)

    i, j = 0, len(disk) - 1

    while i < j:
        while j > i and disk[j] == ".":
            j -= 1
        while i < j and disk[i] != ".":
            i += 1
        disk[i], disk[j] = disk[j], disk[i]

    score = 0
    for index, value in enumerate(disk):
        if value == ".":
            break
        score += index * int(value)

    return score


# PART 2:
def part_two(inp):
    n = len(inp)
    disk = []

    for index, val in enumerate(inp):
        disk.append([
            '.' if index % 2 else str(index//2),
            int(val)
        ])

    return disk


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")[0]

    # print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
