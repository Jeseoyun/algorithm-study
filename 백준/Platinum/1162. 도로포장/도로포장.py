import heapq

INF = float('inf')


def dijkstra(graph, N, start, end, K):
    dist = [[INF]*(N+1) for _ in range(K+1)]  # k를 0번 쓴 경우 ~ K번 쓴 경우까지 저장
    dist[0][start] = 0

    heap = [(0, start, 0)]  # cost, node, used

    while heap:
        curr_cost, curr_node, curr_used = heapq.heappop(heap)

        if curr_cost > dist[curr_used][curr_node]:
            continue

        for next_cost, next_node in graph[curr_node]:
            new_cost = curr_cost + next_cost

            # 1. 그냥 가기
            if new_cost < dist[curr_used][next_node]:
                dist[curr_used][next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node, curr_used))

            # 2. 도로 포장 하고 가기
            if (curr_used < K) and (curr_cost < dist[curr_used+1][next_node]):
                dist[curr_used+1][next_node] = curr_cost
                heapq.heappush(heap, (curr_cost, next_node, curr_used+1))

    return min(dist[k][end] for k in range(K+1))


def main():
    N, M, K = map(int, input().split())
    graph = {node: [] for node in range(1, N+1)}

    for _ in range(M):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))

    dist = dijkstra(graph, N, 1, N, K)
    print(dist)


if __name__ == "__main__":
    main()