import numpy as np
from rich import print
from functools import reduce
import time 
from PIL import Image

def array_to_img(array, index):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]:
                array[i][j] = 255

    mod = np.array(array, dtype=np.uint8)
    image = Image.fromarray(mod)
    image.save(f'images/{index}.png')

def newmat():
    mat = []
    for _ in range(n):
        temp = [0]*m
        mat.append(temp)
    return mat

def matprint(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j] if mat[i][j] else " ", end="")
        print()
    print("\n\n\n")

# PART 1: simulate up upgrading their pos with %
def part_one(inp):
    n, m = 103, 101

    for ind in range(10000):
        for index, (pos, velo) in enumerate(inp):
            y, x = pos
            vy, vx = velo

            dx, dy = (x + vx)%n, (y + vy)%m

            # print(f'{(x, y)} -> {(dx, dy)}')

            inp[index][0][1], inp[index][0][0] = dx, dy

    quadrants = [0]*4
    mid_ver, mid_hor = m//2, n//2

    for pos, _ in inp:
        y, x = pos

        if y > mid_ver:
            if x < mid_hor:
                quadrants[1] += 1
            elif x > mid_hor:
                quadrants[3] += 1
        elif y < mid_ver:
            if x < mid_hor:
                quadrants[0] += 1
            elif x > mid_hor:
                quadrants[2] += 1

    return reduce(lambda x, y: x*y, quadrants)


# PART 2: generate images and find it manually.
def part_two(inp):
    n, m = 103, 101

    for ind in range(10000):
        mat = newmat()
        for index, (pos, velo) in enumerate(inp):
            y, x = pos
            vy, vx = velo

            dx, dy = (x + vx)%n, (y + vy)%m
            mat[dx][dy] += 1

            inp[index][0][1], inp[index][0][0] = dx, dy

        array_to_img(mat, str(ind))
        del mat

    return "Find image in /images folder."


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")
        data = list(map(lambda x: [list(map(int, each[2:].split(','))) for each in x.split()], data))

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
