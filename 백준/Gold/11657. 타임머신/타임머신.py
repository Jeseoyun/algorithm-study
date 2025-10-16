INF = float('inf')
START = 1


def main():
    N, M = map(int, input().split())
    graph = {v: [] for v in range(1, N+1)}

    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))  # C는 가중치

    # print(graph)

    distance = {v: INF for v in graph}
    distance[START] = 0

    for i in range(N-1):
        updated = False

        for u in graph:
            for v, weight in graph[u]:
                if distance[u] != INF and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    updated = True

        if not updated:
            break

    for u in graph:
        for v, weight in graph[u]:
            if distance[u] != INF and distance[u] + weight < distance[v]:
                print(-1)
                return

    for v in range(2, N+1):
        print(distance[v] if distance[v] != INF else -1)


if __name__ == "__main__":
    main()