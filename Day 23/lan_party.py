from collections import defaultdict


# PART 1:
def part_one(inp):
    adj = defaultdict(list)

    for src, dst in inp:
        adj[src].append(dst)
        adj[dst].append(src)

    print(adj)

    visited = set()
    sample = set()

    def dfs(node, history):
        visited.add(node)
        history.append(node)

        print(*history, sep="--")

        if len(history) > 2:
            return sample.add(tuple(sorted(history[-3:])))

        for nei in adj[node]:
            if nei not in visited and all([nei in adj[prev] for prev in history]):
                dfs(nei, history)

        history.pop()
        visited.remove(node)

    for key in adj:
        print("\n\n\n")
        dfs(key, [])

    print("\n\n", *map(' '.join, sorted(sample)), sep="\n")

    return len(sample)


# PART 2:
def part_two(inp):
    pass


def main():
    data = []

    with open("input.txt", "r") as file:
        data = list(map(lambda x: x.split("-"), file.read().split("\n")))

    print("Part 1:", part_one(data))
    # print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
