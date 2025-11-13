from collections import deque


def main():
    n = int(input())
    m = int(input())
    graph = {i: [] for i in range(1, n+1)}
    rgraph = {i: [] for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n+1)}

    for _ in range(m):
        s, d, c = map(int, input().split())
        graph[s].append((d, c))  # 출발지 -> 도착지, 비용
        rgraph[d].append((s, c))  # 도착지 -> 출발지, 비용
        in_degree[d] += 1

    start, end = map(int, input().split())  # 시작 지점, 도착 지점

    queue = deque([i for i in range(1, n+1) if in_degree[i] == 0])
    dist = {i: -1 for i in range(1, n+1)}
    dist[start] = 0

    while queue:
        cur = queue.popleft()

        if dist[cur] != -1:
            for adj, cost in graph[cur]:
                dist[adj] = max(dist[adj], dist[cur] + cost)

        for adj, cost in graph[cur]:
            in_degree[adj] -= 1

            if in_degree[adj] == 0:
                queue.append(adj)

    pass_through = 0
    rqueue = deque([end])
    visited = set([end])

    while rqueue:
        cur = rqueue.popleft()

        for adj, cost in rgraph[cur]:
            if dist[adj] + cost == dist[cur]:
                pass_through += 1

                if adj in visited:
                    continue
                visited.add(adj)
                rqueue.append(adj)

    print(dist[end])
    print(pass_through)


if __name__ == "__main__":
    main()