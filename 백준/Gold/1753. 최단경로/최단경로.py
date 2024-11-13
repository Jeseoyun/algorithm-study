import heapq
import math
from heapq import heappop, heappush


def main():
    V, E = map(int, input().split())
    start = int(input())
    w_graph = {v: [] for v in range(1, V+1)}

    for _ in range(E):
        u, v, w = map(int, input().split())
        w_graph[u].append((w, v))  # weight, vertex

    # print(w_graph)
    distances = {v: math.inf for v in range(1, V+1)}

    min_heap = []
    heapq.heappush(min_heap, (0, start))
    distances[start] = 0

    while min_heap:
        curr_weight, curr_vertex = heapq.heappop(min_heap)

        if curr_weight > distances[curr_vertex]:
            continue

        for adj_weight, adj_vertex in w_graph[curr_vertex]:
            distance = curr_weight + adj_weight
            if distance < distances[adj_vertex]:
                distances[adj_vertex] = distance
                heapq.heappush(min_heap, (distance, adj_vertex))

    for i in distances.values():
        if i == math.inf:
            print("INF")
        else:
            print(i)

if __name__ == "__main__":
    main()