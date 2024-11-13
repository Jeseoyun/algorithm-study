max_len = 0


def dfs(graph, curr, visited, depth=1):
    global max_len
    visited.append(curr)

    for adj in graph[curr]:
        if adj not in visited:
            dfs(graph, adj, visited.copy(), depth+1)
            max_len = max(max_len, depth+1)


def main():
    global max_len
    T = int(input())

    for test_case in range(1, T+1):
        max_len = 1

        N, M = map(int, input().split())
        graph = {n: [] for n in range(1, N+1)}

        for _ in range(M):
            x, y = map(int, input().split())
            graph[x].append(y)
            graph[y].append(x)
        # print(graph)

        for i in graph.keys():
            visited = []
            dfs(graph, i, visited)
        print(f"#{test_case} {max_len}")


if __name__ == "__main__":
    main()
