def farm_data(data):
    locks, keys = [], []

    while data:

        temp = []
        while data:
            line = data.pop(0)
            if not line:
                break
            temp.append(line)

        pins = []
        for j in range(5):
            pin = 0
            for i in range(1, 6):
                if temp[i][j] == "#":
                    pin += 1
            pins.append(pin)


        if all([char == '#' for char in temp[0]]):
            locks.append(pins)
        else:
            keys.append(pins)

    return locks, keys


# PART 1:
def part_one(inp):
    locks, keys = inp

    def check_fit(lock, key):
        for i in range(5):
            if lock[i] + key[i] > 5:
                return False
        return True

    fit = 0
    for lock in locks:
        for key in keys:
            if check_fit(lock, key):
                fit += 1



    return fit


# PART 2:
def part_two(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")
        data = farm_data(data)

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
