
def dfs(N, r, placed, cols, d1, d2):
    if r == N:
        return 1

    total = 0

    for c in range(N):
        if c in cols or (r-c) in d1 or (r+c) in d2:
            continue

        placed.add((r, c))
        cols.add(c)
        d1.add(r-c)
        d2.add(r+c)

        total += dfs(N, r+1, placed, cols, d1, d2)

        placed.remove((r, c))
        cols.remove(c)
        d1.remove(r-c)
        d2.remove(r+c)

    return total


def main():
    N = int(input())

    # possible = set()
    possible = dfs(N, 0, set(), set(), set(), set())
    print(possible)
    # print(len(possible))


if __name__ == "__main__":
    main()
