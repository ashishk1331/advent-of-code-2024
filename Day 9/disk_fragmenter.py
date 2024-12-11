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

    disk = []
    for index, value in enumerate(inp):
        if int(value) > 0:
            disk.extend(["." if index % 2 else str(index // 2)] * int(value))

    i = j = len(disk) - 1
    while j > 0:

        while disk[i] != "." and disk[i - 1] == disk[i]:
            i -= 1

        if disk[i] != ".":
            file = j - i + 1

            a = b = 0
            while a < i:

                while disk[a] == "." and disk[a] == disk[a + 1]:
                    a += 1

                slot = a - b + 1
                if disk[a] == "." and slot >= file:
                    break

                a += 1
                b = a

            for index in range(file):
                disk[i + index], disk[b + index] = disk[b + index], disk[i + index]

        i -= 1
        j = i

    score = 0
    for index, value in enumerate(disk):
        if value != ".":
            score += index * int(value)

    return score


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")[0]

    # print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
