from collections import deque


INF = float('inf')


def main():
    N, M = map(int, input().split())
    order_graph = {node: [] for node in range(1, N+1)}

    for _ in range(M):
        n, *order = map(int, input().split())

        for idx in range(n-1):
            order_graph[order[idx]].append(order[idx+1])

    in_degree = {node: 0 for node in range(1, N+1)}
    for node in order_graph:
        for adj in order_graph[node]:
            in_degree[adj]+= 1

    queue = deque([i for i in in_degree if in_degree[i] == 0])
    result = []

    # 진입 차수가 0인놈들 추출
    # 연결 끊어주기
    # 끊은 후 다시 진입차수 0인놈들 큐에 삽입
    while queue:
        # print(queue)
        cur = queue.popleft()
        result.append(cur)

        for adj in order_graph[cur]:
            in_degree[adj] -= 1

            if in_degree[adj] == 0:
                queue.append(adj)

    if len(result) == N:
        print(*result, sep="\n")
    else:
        print(0)


if __name__ == "__main__":
    main()