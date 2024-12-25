from rich import print

directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}


def find_robot(layout):
    for i in range(len(layout)):
        for j in range(len(layout[0])):
            if layout[i][j] == "@":
                return i, j


def get_first_stone(layout, position, direction):
    (sx, sy), (dx, dy) = position, direction

    while layout[sx][sy] != "#":
        sx, sy = sx + dx, sy + dy
    return sx, sy


def can_move(position, stone):
    (x, y), (sx, sy) = position, stone

    return (abs(x - sx) + abs(y - sy)) > 1


def move_up(layout, position, stone, move):
    (x, y), (sx, sy) = position, stone

    count = 0
    for i in range(1, x - sx + 1):
        if layout[x - i][y] == "O":
            count += 1

    startx = sx + 1

    while count:
        layout[startx][y] = "O"
        startx += 1
        count -= 1

    layout[startx][y] = "@"

    newhead = (startx, y)
    # print(f"moved head from {position} to {newhead}", layout[startx][y])

    startx += 1

    while startx <= x:
        layout[startx][y] = "."
        startx += 1

    return newhead


def move_right(layout, position, stone, move):
    (x, y), (sx, sy) = position, stone

    count = 0
    for i in range(1, sy - y + 1):
        if layout[x][y + i] == "O":
            count += 1

    starty = sy - 1

    while count:
        layout[x][starty] = "O"
        starty -= 1
        count -= 1

    layout[x][starty] = "@"

    newhead = (x, starty)
    # print(f"moved head from {position} to {newhead}", layout[startx][y])

    starty -= 1

    while starty >= y:
        layout[x][starty] = "."
        starty -= 1

    return newhead


# PART 1:
def part_one(inp):
    layout, moves = inp["layout"], inp["moves"]
    robot = find_robot(layout)

    for move in moves[:4]:
        dx, dy = directions[move]
        stone = get_first_stone(layout, robot, directions[move])

        if not can_move(robot, stone):
            print(f"Can't move from {robot} towards {stone}.")
            continue
        else:

            if move == "^":
                # print("Layout before move_up:", layout)
                robot = move_up(layout, robot, stone, move)
                # print("Layout after move_up:", layout)
            elif move == ">":
                robot = move_right(layout, robot, stone, move)
            elif move == "<":
                pass
            elif move == "v":
                pass
            print("Updated")

    return layout


# PART 2:
def part_two(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")

        layout = []
        while True:
            level = data.pop(0)
            if not level:
                break
            layout.append([char for char in level])

        moves = ""
        while data:
            moves += data.pop(0)

        data = {
            "layout": layout,
            "moves": moves,
        }

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()