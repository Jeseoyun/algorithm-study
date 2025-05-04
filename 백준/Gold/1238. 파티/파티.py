import heapq


def dijkstra(graph, start):
    dist = {key: float('inf') for key in graph.keys()}

    heap = [(0, start)]
    dist[start] = 0

    while heap:
        curr_cost, curr_node = heapq.heappop(heap)
        # print(curr_node, curr_cost, dist)

        for neighbor_cost, neighbor in graph[curr_node]:
            cost = dist[curr_node] + neighbor_cost
            if dist[neighbor] > cost:
                dist[neighbor] = cost
                heapq.heappush(heap, (cost, neighbor))

    return dist


def main():
    N, M, X = map(int, input().split())  # 노드 수, 간선 수, 도착 지점
    village = {i: [] for i in range(1, N+1)}

    for _ in range(M):
        start, end, cost = map(int, input().split())
        village[start].append((cost, end))

    max_time = 0
    for student in village.keys():
        depart_dist = dijkstra(village, student)
        arrive_dist = dijkstra(village, X)

        max_time = max(max_time, depart_dist[X] + arrive_dist[student])

    print(max_time)


if __name__ == "__main__":
    main()