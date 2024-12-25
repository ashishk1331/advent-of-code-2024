# PART 1:
def part_one(inp):
    registers, program = inp["registers"], inp["program"]
    output = []

    ind = 0
    while ind < len(program):
        opcode, literal = program[ind : ind + 2]

        combo = literal
        if literal == 4:
            combo = registers["A"]
        elif literal == 5:
            combo = registers["B"]
        elif literal == 6:
            combo = registers["C"]

        if opcode == 0:
            registers["A"] //= 2**combo
        elif opcode == 1:
            registers["B"] ^= literal
        elif opcode == 2:
            registers["B"] = combo % 8
        elif opcode == 3 and registers["A"] != 0:
            ind = literal * 2
            continue
        elif opcode == 4:
            registers["B"] ^= registers["C"]
        elif opcode == 5:
            output.append(combo % 8)
        elif opcode == 6:
            registers["B"] = registers["A"] // (2**combo)
        elif opcode == 7:
            registers["C"] = registers["A"] // (2**combo)

        ind += 2

    return ",".join(map(str, output))


# PART 2:
def part_two(inp):
    registers, program = inp["registers"], inp["program"]

    original = "".join(map(str, program))

    value = 0
    while True:

        registers["A"] = value

        # print(value)

        out = part_one({"registers": registers, "program": program})

        if out == original:
            return value

        # print("Out: ", out, "Original:", original)
        value += 1

    return part_one(inp)


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")
        registers = {}
        while True:
            line = data.pop(0)

            if not line:
                break

            name, value = list(map(str.strip, line.split(":")))
            value = int(value)
            name = name[-1:]

            registers[name] = value

        program = list(map(int, data.pop()[8:].strip().split(",")))

        data = {
            "registers": registers,
            "program": program,
        }

    # print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
