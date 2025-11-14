import heapq
from heapq import heappush

INF = float('inf')


def main():
    N = int(input())
    M = int(input())

    graph = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))

    start, end = map(int, input().split())

    heap = [(0, start)]

    costs = {i: INF for i in range(1, N+1)}
    costs[start] = 0

    while heap:
        cur_cost, cur = heapq.heappop(heap)

        if cur_cost > costs[cur]:
            continue

        for adj, adj_cost in graph[cur]:
            new_cost = cur_cost + adj_cost

            if new_cost < costs[adj]:
                costs[adj] = new_cost
                heapq.heappush(heap, (new_cost, adj))

    print(costs[end])


if __name__ == "__main__":
    main()