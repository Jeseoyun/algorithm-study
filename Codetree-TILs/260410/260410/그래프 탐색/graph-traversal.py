def dfs(edges, visited, curr):
    for adj in edges[curr]:
        if adj in visited:
            continue

        visited.add(adj)
        dfs(edges, visited, adj)

    return 1


def main():
    N, M = map(int, input().split())
    edges = dict()

    if M == 0:  # 연결된 노드 없음
        print(0)
        return

    for _ in range(M):
        x, y = map(int, input().split())
        if x not in edges.keys():
            edges[x] = []
        if y not in edges.keys():
            edges[y] = []

        edges[x].append(y)
        edges[y].append(x)

    start = 1
    visited = {start}

    dfs(edges, visited, start)

    print(len(visited)-1)  # 자기 자신 제외


if __name__ == "__main__":
    main()