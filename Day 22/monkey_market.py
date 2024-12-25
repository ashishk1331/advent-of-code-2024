mul64 = lambda x: ((x * 64) ^ x) % 16777216
div32 = lambda x: ((x // 32) ^ x) % 16777216
mul2048 = lambda x: ((x * 2048) ^ x) % 16777216
find = lambda x: mul2048(div32(mul64(x)))


# PART 1:
def part_one(inp):
    mus = 0
    for buyer in inp:
        for _ in range(2000):
            n = find(buyer)
            buyer = n
        mus += buyer

    return mus


# PART 2:
def part_two(inp):
    temp = 123

    fermi = lambda x, y: f'{str(temp).rjust(8)}: {x%10} ({y})'

    print(fermi(temp, 0))
    for _ in range(10):
        nxt = find(temp)
        print(fermi(nxt, nxt%10 - temp%10))
        temp = nxt

    return None


def main():
    data = []

    with open("input.txt", "r") as file:
        data = list(map(int, file.read().split("\n")))

    # print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
