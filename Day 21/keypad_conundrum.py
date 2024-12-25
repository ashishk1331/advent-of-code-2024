from rich import print


# PART 1:
def part_one(inp):

    ndash = "789456123B0A"
    ddash = "B^A<v>"

    # numpad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
    nmap = {
        ('0', '1'): '^<',
        ('0', '4'): '^<^', # '^^<'
        ('0', '7'): '^<^^', # '^^<^' '^^^<'
        ('A', '1'): '^<<', # '<^<'
        ('A', '4'): '^<<^', # '^^<<' '^<^<' '<^^<' '<^<^' '^<<^'
        ('A', '7'): '^<<^^',
        ('1', '0'): '>v',
        ('1', 'A'): '>>v',
        ('4', '0'): '>vv',
        ('4', 'A'): '>>vv',
        ('7', '0'): '>vvv',
        ('7', 'A'): '>>vvv',
    }
    # direcpad = [[None, "^", "A"], ["<", "v", ">"]]
    dmap = {
        ('<', '^'): '>^',
        ('<', 'A'): '>>^',
        ('^', '<'): 'v<',
        ('A', '<'): 'v<<',
    }

    def find_num(num):
        index = ndash.find(num)
        return index // 3, index % 3

    def find_direc(direc):
        index = ddash.find(direc)
        return index // 3, index % 3

    def num_to_direc(cmd):
        init = (3, 2)
        res = ""

        for char in cmd:
            nx, ny = find_num(char)
            dx, dy = init[0] - nx, init[1] - ny

            index = init[0]*3 + init[1]
            if (ndash[index], char) in nmap:
                res += nmap[(ndash[index], char)]
                continue

            mov = ""

            if dy < 0:
                mov += ">" * abs(dy)
            if dx < 0:
                mov += "v" * abs(dx)
            if dx > 0:
                mov += "^" * dx
            if dy > 0:
                mov += "<" * dy

            res += mov + "A"
            init = (nx, ny)

        return res

    def direc_to_direc(cmd):
        init = (0, 2)
        res = ""

        for char in cmd:
            nx, ny = find_direc(char)
            dx, dy = init[0] - nx, init[1] - ny

            index = init[0]*3 + init[1]
            if (ddash[index], char) in dmap:
                res += dmap[(ddash[index], char)]
                continue

            mov = ""

            if dx > 0:
                mov += "^" * dx
            if dy > 0:
                mov += "<" * dy
            if dy < 0:
                mov += ">" * abs(dy)
            if dx < 0:
                mov += "v" * abs(dx)

            res += mov + "A"
            init = (nx, ny)

        return res

    score = 0

    for cmd in inp:
        # print(cmd)
        mov = num_to_direc(cmd)
        # print(mov)
        mov = direc_to_direc(mov)
        # print(mov)
        mov = direc_to_direc(mov)
        # print(mov)

        length = len(mov)
        num = int(cmd[:-1])

        print(cmd, length, num)

        score += length * num

    return score


# PART 2:
def part_two(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
