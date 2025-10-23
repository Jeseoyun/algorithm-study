import heapq

INF = float('inf')


def dijkstra(graph, N, oil, start, end):
    dist = [[INF]*(max(oil.values())+1) for _ in range(N+1)]
    # print(dist)
    heap = [(0, start, oil[start])]  # cost, node, min_oil
    dist[start][oil[start]] = 0

    while heap:
        curr_cost, curr_node, prev_min_oil = heapq.heappop(heap)
        # print("curr_node:", curr_node, "curr_cost:", curr_cost, "prev_min_oil:", prev_min_oil)
        # print(dist)

        if dist[curr_node][prev_min_oil] < curr_cost:
            continue

        for next_cost, next_node in graph[curr_node]:
            new_cost = curr_cost + next_cost * prev_min_oil
            # print(new_cost)

            if dist[next_node][prev_min_oil] > new_cost:
                dist[next_node][prev_min_oil] = new_cost
                heapq.heappush(heap, (new_cost, next_node, min(oil[next_node], prev_min_oil)))

    return min(dist[end])


def main():
    N, M = map(int, input().split())  # 도시 수, 도로 수
    s_oil = {idx+1: val for idx, val in enumerate(map(int, input().split()))}

    road = {node: [] for node in range(1, N+1)}
    for _ in range(M):
        a, b, d = map(int, input().split())
        road[a].append((d, b))
        road[b].append((d, a))

    # print(s_oil, road)

    dist = dijkstra(road, N, s_oil, 1, N)
    print(dist)


if __name__ == "__main__":
    main()