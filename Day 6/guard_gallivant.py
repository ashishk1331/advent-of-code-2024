from rich import print


def get_guard_position(inp):
    n, m = len(inp), len(inp[0])
    for i in range(n):
        for j in range(m):
            if inp[i][j] == "^":
                return (i, j)


# PART 1:
def part_one(inp):
    n, m = len(inp), len(inp[0])
    row, col = get_guard_position(inp)
    directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    next_direc = {">": "v", "v": "<", "<": "^", "^": ">"}
    visited = set()

    while True:
        symbol = inp[row][col]

        dx, dy = directions[symbol]
        x, y = row + dx, col + dy

        if x not in range(n) or y not in range(m):
            break

        if inp[x][y] == "#":
            symbol = next_direc[inp[row][col]]
            dx, dy = directions[symbol]
            row, col = row + dx, col + dy
        else:
            row, col = x, y

        inp[row][col] = symbol
        visited.add((row, col))

    return len(visited)


# PART 2:
def part_two(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = list(map(lambda x: [i for i in x], file.read().split("\n")))

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
