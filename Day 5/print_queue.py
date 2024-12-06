from rich import print
from collections import defaultdict


def isvalid(seq, adj):
    visited = set()

    for i, page in enumerate(seq):
        for j in range(i - 1, -1, -1):
            if seq[j] not in adj[page] or seq[j] not in visited:
                return False
        visited.add(page)

    return True


# PART 1: create a adjency matrix and check for predecessors in the list
def part_one(inp):
    deps, seq = inp[0], inp[1]

    adj = defaultdict(list)
    for req, val in deps:
        adj[val].append(req)

    valid_seq = [each for each in seq if isvalid(each, adj)]

    middle = 0
    for each in valid_seq:
        middle += each[len(each) // 2]

    return middle


# PART 2:
def part_two(inp):
    deps, seq = inp[0], inp[1]

    adj = defaultdict(list)
    for req, val in deps:
        adj[val].append(req)

    print(adj)
    valid_seq = [each for each in seq if not isvalid(each, adj)]

    middle = 0
    for each in valid_seq:
        middle += each[len(each) // 2]

    return middle


def main():
    data = []

    with open("input.txt", "r") as file:
        inp = file.read().split("\n")
        deps = []
        index = 0
        while inp[index] != "":
            deps.append(tuple(map(int, inp[index].split("|"))))
            index += 1

        seq = [tuple(map(int, s.split(","))) for s in inp[index + 1 :]]

        data = [deps, seq]

    # print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
