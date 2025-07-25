def dfs(N, M, i, curr, visited, result):
    if i == M:
        result.append(curr)
        return

    for j in range(1, N+1):
        if visited[j] == 1:
            continue
        
        visited[j] = 1
        dfs(N, M, i+1, curr+[j], visited, result)
        visited[j] = 0


def main():
    N, M = map(int, input().split())

    result = []
    visited = [0]*(N+1)

    dfs(N, M, 0, [], visited, result)

    for res in result:
        print(*res)
    # print(result)


if __name__ == "__main__":
    main()