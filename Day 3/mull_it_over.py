import re


# PART 1: regex to find mul instructions
def part_one(inp):
    inst = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp)
    return sum([int(x) * int(y) for x, y in inst])


# PART 2: regex to find mul, do and don't instructions
def part_two(inp):
    regex = r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))"
    inst = re.findall(regex, inp)
    inst = [list(filter(bool, x)) for x in inst]

    mus, cont = 0, True
    for each in inst:
        opcode = each[0]
        if opcode.startswith("mul"):
            if cont:
                mus += int(each[1]) * int(each[2])
        elif opcode.startswith("don't"):
            cont = False
        else:
            cont = True

    return mus


def main():
    input = []

    with open("input.txt", "r") as file:
        input = file.read()

    # print(part_one(input))
    print(part_two(input))


if __name__ == "__main__":
    main()
