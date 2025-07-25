def dfs(n, m, step, curr, visited, result):
    if step == m:
        result.append(curr)
        return

    for i in range(1, n+1):
        if visited[i] == 1:
            continue

        visited[i] = 1
        dfs(n, m, step+1, curr+[i], visited, result)
        visited[i] = 0


def main():
    N, M = map(int, input().split())

    result = []
    visited = [0]*(N+1)
    dfs(N, M, 0, [], visited, result)

    for res in result:
        print(*res)


if __name__ == "__main__":
    main()