# PART 1:
def part_one(data):
    pass


# PART 2:
def part_two(data):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
