from collections import defaultdict


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def insert(array):
    head = p = None
    for ele in array:
        if p is None:
            p = Node(ele)
            head = p
        else:
            p.right = Node(ele)
            p.right.left = p
            p = p.right
    return head


def dll_length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.right
    return count


# PART 1:
def part_one(inp):
    head = insert(inp)

    for level in range(25):
        p = head
        while p is not None:

            ele = p.value
            string = str(p.value)
            length = len(string)

            if ele == 0:
                p.value = 1
            elif length % 2:  # odd length
                p.value *= 2024
            else:  # even length
                left_val, right_val = int(string[: length // 2]), int(
                    string[length // 2 :]
                )
                q = p.right

                p.value = left_val
                n = Node(right_val)

                p.right = n
                n.left = p

                n.right = q
                if q:
                    p.left = n

                p = p.right

            p = p.right

    return dll_length(head)


# PART 2:
def part_two(inp):
    visited = defaultdict(lambda: 0)

    for ele in inp:
        visited[ele] += 1

    for level in range(75):
        temp = defaultdict(lambda: 0)
        for key, freq in visited.items():

            string = str(key)
            length = len(string)

            if key == 0:
                temp[1] += freq
            elif length % 2:
                temp[key * 2024] += freq
            else:
                left_val, right_val = int(string[: length // 2]), int(
                    string[length // 2 :]
                )

                temp[left_val] += freq
                temp[right_val] += freq

        del visited
        visited = temp

    return sum(visited.values())


def main():
    data = []

    with open("input.txt", "r") as file:
        data = list(map(int, file.read().split("\n")[0].split()))

    print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))


if __name__ == "__main__":
    main()
