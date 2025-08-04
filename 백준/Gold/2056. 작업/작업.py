from collections import deque


def main():
    N = int(input())

    graph = {i: [] for i in range(1, N+1)}
    in_degree = {i: 0 for i in range(1, N+1)}
    costs = {i: 0 for i in range(1, N+1)}
    for node in range(1, N+1):
        cost, n, *pre_works = input().split()
        cost, n, pre_works = int(cost), int(n), list(map(int, pre_works))
        costs[node] = cost
        in_degree[node] += n
        for pw in pre_works:
            graph[pw].append(node)

    queue = deque()
    dp = [0 for _ in range(N+1)]

    for node in range(1, N+1):
        if in_degree[node] == 0:
            queue.append(node)
            dp[node] += costs[node]

    while queue:
        # print(queue)
        curr = queue.popleft()

        for adj in graph[curr]:
            in_degree[adj] -= 1
            dp[adj] = max(dp[adj], dp[curr]+costs[adj])
            # print(dp)

            if in_degree[adj] == 0:
                queue.append(adj)

    print(max(dp))


if __name__ == "__main__":
    main()