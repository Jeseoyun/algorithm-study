def combination(n, m, idx, curr, result):
    if len(curr) == m:
        result.append(curr)
        return

    if idx > n:
        return

    combination(n, m, idx+1, curr+[idx], result)
    combination(n, m, idx+1, curr, result)


def main():
    N, M = map(int, input().split())

    result = []
    combination(N, M, 1, [], result)

    for res in result:
        print(*res)


if __name__ == "__main__":
    main()