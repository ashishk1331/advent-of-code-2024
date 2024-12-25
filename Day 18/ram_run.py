from rich import print


def pprint(array):
    print(*list(map("".join, array)), sep="\n")


# PART 1:
def part_one(inp):

    size = 7
    disk = [["."] * size for _ in range(size)]

    for y, x in inp:
        disk[x][y] = "#"

    pprint(disk)

    return 0


# PART 2:
def part_two(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = list(
            map(lambda x: list(map(int, x.split(","))), file.read().split("\n"))
        )

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
