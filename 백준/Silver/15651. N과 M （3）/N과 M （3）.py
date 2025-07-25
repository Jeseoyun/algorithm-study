def dfs(n, m, step, curr, result):
    if step == m:
        result.append(curr)
        return

    for i in range(1, n+1):
        dfs(n, m, step+1, curr+[i], result)


def main():
    N, M = map(int, input().split())

    result = []
    dfs(N, M, 0, [], result)

    for res in result:
        print(*res)


if __name__ == "__main__":
    main()