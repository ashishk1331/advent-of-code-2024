# PART 1:
def part_one(inp):
    n, m = len(inp), len(inp[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    fenced = set()

    def area_peri(row, col, char):
        
        visited.add((row, col))

        area = 1
        peri = 0

        for dx, dy in directions:
            x, y = row + dx, col + dy

            if (
                0 <= x < n
                and 0 <= y < m
                and inp[x][y] == char
            ):
                if (x, y) not in visited:
                    sub_area, sub_peri = area_peri(x, y, char)
                    area += sub_area
                    peri += sub_peri
            else:
                peri += 1

        return area, peri


    cost = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                area, peri = area_peri(i, j, inp[i][j])
                cost += area*peri

    return cost


# PART 2:
def part_two(inp):
    n, m = len(inp), len(inp[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pairwise = [
        [(-1, 0), (0, 1)],
        [(0, 1), (1, 0)],
        [(1, 0), (0, -1)],
        [(0, -1), (-1, 0)],
    ]
    visited = set()
    fenced = set()

    def find_sides(row, col, char, prev_dx, prev_dy):
        
        visited.add((row, col))

        area = 1
        corners = 0

        for dx, dy in directions:
            x, y = row + dx, col + dy

            if (
                0 <= x < n
                and 0 <= y < m
                and inp[x][y] == char
                and (x, y) not in visited
            ):
                sub_area, sub_corners = find_sides(x, y, char, dx, dy)
                area += sub_area
                corners += sub_corners

        return area, corners

    cost = 0
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                print(inp[i][j], find_sides(i, j, inp[i][j], 0, 0))

    return cost


def main():
    data = []

    with open("input.txt", "r") as file:
        data = list(map(lambda x: [c for c in x], file.read().split("\n")))

    # print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
