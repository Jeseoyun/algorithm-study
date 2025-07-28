from collections import deque


def main():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())  # 건물 수, 규칙 수
        D = list(map(int, input().split()))  # 건설 비용

        graph = {i: [] for i in range(1, N+1)}
        in_degree = {i: 0 for i in range(1, N+1)}
        for _ in range(K):
            start, end = map(int, input().split())
            graph[start].append(end)
            in_degree[end] += 1

        W = int(input())  # target

        queue = deque()
        dp = [0]*(N+1)
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)
                dp[node] = D[node-1]

        # print(graph)
        # print(in_degree)

        while queue:
            # print(queue, dp)
            node = queue.popleft()

            for neighbor in graph[node]:
                dp[neighbor] = max(dp[neighbor], dp[node]+D[neighbor-1])
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        print(dp[W])


if __name__ == "__main__":
    main()