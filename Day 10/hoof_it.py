# PART 1:
def part_one(inp):
    n, m = len(inp), len(inp[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(row, col, visited):
        if inp[row][col] == 9 and (row, col) not in visited:
            visited.add((row, col))
            return 1

        trail_ends = 0

        for dx, dy in directions:
            x, y = row + dx, col + dy

            if 0 <= x < n and 0 <= y < m and inp[x][y] == inp[row][col] + 1:
                trail_ends += dfs(x, y, visited)

        return trail_ends

    score = 0
    for i in range(n):
        for j in range(m):
            if inp[i][j] == 0:
                visited = set()
                score += dfs(i, j, visited)

    return score


# PART 2:
def part_two(inp):
    n, m = len(inp), len(inp[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(row, col):
        if inp[row][col] == 9:
            return 1

        trail_ends = 0

        for dx, dy in directions:
            x, y = row + dx, col + dy

            if 0 <= x < n and 0 <= y < m and inp[x][y] == inp[row][col] + 1:
                trail_ends += dfs(x, y)

        return trail_ends

    score = 0
    for i in range(n):
        for j in range(m):
            if inp[i][j] == 0:
                score += dfs(i, j)

    return score


def main():
    data = []

    with open("input.txt", "r") as file:
        data = [list(map(int, [x for x in row])) for row in file.read().split("\n")]

    print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
