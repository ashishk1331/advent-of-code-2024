from rich import print


# PART 1:
def part_one(inp):
    ops = {
        "AND": lambda x, y: x & y,
        "OR": lambda x, y: x | y,
        "XOR": lambda x, y: x ^ y,
    }

    def evaluate(wire):
        mode = inp[wire]

        if mode["type"] == "var":
            return mode["value"]
        else:
            return ops[mode["op"]](*map(evaluate, mode["params"]))

    res = 0
    for wire in inp:
        if wire.startswith("z"):
            index = int(wire[1:])
            res += evaluate(wire) * (2**index)

    return res


# PART 2:
def part_two(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = file.read().split("\n")

        wires = {}
        while True:
            line = data.pop(0)
            if not line:
                break
            wire, value = list(map(str.strip, line.split(":")))
            wires[wire] = {"type": "var", "value": int(value)}

        while data:
            line = data.pop()
            inp1, op, inp2, _, out = line.split()
            wires[out] = {
                "type": "fn",
                "op": op,
                "params": (inp1, inp2),
            }

    print("Part 1:", part_one(wires))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
