import heapq


def prim(graph):
    visited = set()
    start = 1
    min_heap = [[w, start, e] for e, w in graph[start]]
    heapq.heapify(min_heap)
    visited.add(start)

    total_weight = 0
    while min_heap:
        weight, start, end = heapq.heappop(min_heap)

        if end in visited:
            continue

        visited.add(end)
        total_weight += weight

        for v, w in graph[end]:
            if v in visited:
                continue

            heapq.heappush(min_heap, [w, end, v])

    return total_weight


def main():
    V, E = map(int, input().split())
    graph = {i: [] for i in range(1, V+1)}

    for _ in range(E):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))

    # print(graph)
    min_weight = prim(graph)
    print(min_weight)


if __name__ == "__main__":
    main()