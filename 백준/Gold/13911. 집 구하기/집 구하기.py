import heapq


INF = float('inf')


def dijkstra(graph, starts, threshold):
    dist = {node: INF for node in graph}
    heap = []

    for start in starts:
        heapq.heappush(heap, (0, start))
        dist[start] = 0

    while heap:
        curr_dist, curr_node = heapq.heappop(heap)

        for next_dist, next_node in graph[curr_node]:
            new_dist = curr_dist + next_dist

            if new_dist > threshold:
                continue

            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return dist


def main():
    V, E = map(int, input().split())
    graph = {v: [] for v in range(1, V+1)}

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))  # 가중치, 도착지점
        graph[v].append((w, u))

    # print(graph)

    M, x = map(int, input().split())  # 맥 수, 맥 거리 기준
    mcdonalds = list(map(int, input().split()))  # 맥 위치

    S, y = map(int, input().split())  # 스 수, 스 거리 기준
    starbucks = list(map(int, input().split()))  # 스 위치

    store = set(mcdonalds+starbucks)

    m_dist= dijkstra(graph, mcdonalds, x)  # 맥 거리
    s_dist= dijkstra(graph, starbucks, y)  # 스 거리

    # 3. 맥 & 스 교집합 중 거리 합 최소인 집
    min_dist = INF

    for node in graph:
        if node in store:
            continue

        if m_dist[node] > x or s_dist[node] > y:
            continue

        min_dist = min(min_dist, m_dist[node]+s_dist[node])

    print(min_dist if min_dist!= INF else -1)


if __name__ == "__main__":
    main()