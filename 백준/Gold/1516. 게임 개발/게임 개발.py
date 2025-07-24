from collections import deque


def main():
    N = int(input())
    graph = {i+1: [] for i in range(N)}
    costs = {i+1: 0 for i in range(N)}
    in_degree = {i+1: 0 for i in range(N)}

    dp = [0 for _ in range(N+1)]

    # 1. 그래프 만들기
    for end in range(1, N+1):
        cost, *edges = map(int, input().split())
        costs[end] = cost
        # print(edges[:-1])
        for start in edges[:-1]:
            graph[start].append(end)
            in_degree[end] += 1
    # print(graph, costs, in_degree)

    # 2. 큐 초기값 넣기
    queue = deque()
    for node in range(1, N+1):
        if in_degree[node] == 0:
            queue.append(node)
            dp[node] = costs[node]

    while queue:
        curr = queue.popleft()
        # print("curr",curr)

        for neighbor in graph[curr]:
            # print("  neighbor",neighbor)
            in_degree[neighbor] -= 1
            # print(dp[neighbor], dp[curr]+costs[neighbor])
            dp[neighbor] = max(dp[neighbor], dp[curr]+costs[neighbor])

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    for i in dp[1:]:
        print(i)


if __name__ == "__main__":
    main()