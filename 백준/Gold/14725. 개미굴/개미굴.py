from collections import defaultdict


def add_depth(tree, arr):
    if len(arr) == 0:
        return

    if arr[0] not in tree:
        tree[arr[0]] = {}

    add_depth(tree[arr[0]], arr[1:])


def print_tree(tree, depth):
    for elem in sorted(tree.keys()):
        print("--" * depth, elem, sep='')
        print_tree(tree[elem], depth+1)


def main():
    n = int(input())
    ant_cave = defaultdict(list)

    for _ in range(n):
        sn, *search = input().split()
        add_depth(ant_cave, search)

    print_tree(ant_cave, 0)


if __name__ == "__main__":
    main()