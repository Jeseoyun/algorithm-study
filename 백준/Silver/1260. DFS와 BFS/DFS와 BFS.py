from collections import deque


def dfs(curr, visited):
    visited.append(curr)

    if len(visited) == N:
        return list(map(str, visited))

    for adj in adj_list[curr]:
        if adj not in visited:
            dfs(adj, visited)

    return list(map(str, visited))


def bfs():
    visited = []
    queue = deque()

    queue.append(V)
    visited.append(V)

    while queue:
        curr = queue.popleft()
        for adj in adj_list[curr]:
            if adj in visited:
                continue

            queue.append(adj)
            visited.append(adj)
    return list(map(str, visited))


N, M, V = map(int, input().split())  # vertex 수, edge 수, 탐색 시작 정점
edges = [list(map(int, input().split())) for _ in range(M)]

adj_list = {v: [] for v in range(1, N+1)}

for edge in edges:
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])

adj_list = {adj: sorted(adj_list[adj]) for adj in adj_list}

print(" ".join(dfs(V, [])))
print(" ".join(bfs()))