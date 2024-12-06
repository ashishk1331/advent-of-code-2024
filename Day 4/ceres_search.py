from collections import deque


# PART 1:
def part_one(inp):
    n, m = len(inp), len(inp[0])
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    next_char = {"X": "M", "M": "A", "A": "S", "S": "X"}

    def bfs(row: int, col: int, char: str) -> int:
        q = deque([(row, col, char)])
        count = 0

        while q:
            row, col, char = q.popleft()
            visited.add((row, col))

            if char == "S":
                count += 1

            for dx, dy in directions:
                x, y = row + dx, col + dy

                if x in range(n) and y in range(m) and (x, y) not in visited:
                    if inp[x][y] == "X":
                        q.append((x, y, "X"))
                    elif inp[x][y] == next_char[char]:
                        q.append((x, y, next_char[char]))

        return count

    count = 0

    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and inp[i][j] == "X":
                count += bfs(i, j, "X")

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
