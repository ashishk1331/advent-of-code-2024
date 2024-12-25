from rich import print


def find_start(inp):
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == "S":
                return i, j


def find_end(inp):
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == "E":
                return i, j


# PART 1:
def part_one(inp):
    start, end = find_start(inp), find_end(inp)
    n, m = len(inp), len(inp[0])
    #               S        N        E       W
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    arrows = {
        directions[index]: arrow for index, arrow in enumerate(["v", "^", ">", "<"])
    }
    visited = set()
    res = [float("inf")]

    def dfs(row, col, prevx, prevy, score):
        if inp[row][col] == "E":
            print(list(map("".join, inp)), score)
            res[0] = min(res[0], score)
            return

        if res[0] < score:
            return

        prev = inp[row][col]

        visited.add((row, col))
        inp[row][col] = arrows[(prevx, prevy)]

        for dx, dy in directions:
            x, y = row + dx, col + dy

            if 0 <= x < n and 0 <= y < m and (x, y) not in visited and inp[x][y] != "#":
                temp = 1 if (dx, dy) == (prevx, prevy) else 1001
                dfs(x, y, dx, dy, score + temp)

        visited.remove((row, col))
        inp[row][col] = prev

    dfs(*start, *directions[2], 0)

    return res[0]


# PART 2:
def part_two(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = list(map(lambda x: [e for e in x], file.read().split("\n")))

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
