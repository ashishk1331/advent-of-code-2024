from collections import deque


# PART 1:
def part_one(inp):
    n, m = len(inp), len(inp[0])
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    next_char = {
        'X': 'M',
        'M': 'A',
        'A': 'S'
    }

    def bfs(row, col):

        visited.add((row, col))

        if inp[row][col] == 'S':
            return 1

        count = 0
        for dx, dy in directions:
            x, y = row + dx, col + dy

            if (
                0 <= x < n
                and 0 <= y < m
                and next_char[inp[row][col]] == inp[x][y]
                and (x, y) not in visited
            ):
                count += bfs(x, y)

        return count

    count = 0
    for i in range(n):
        for j in range(m):
            if inp[i][j] == "X" and (i, j) not in visited:
                count += bfs(i, j)

    return count


# PART 2:
def part_two(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = list(map(lambda x: [char for char in x], file.read().split("\n")))

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
