
def dfs(start, graph):
    visited = set([start])
    stack = [start]
    cnt = 0

    while stack:
        node = stack.pop()
        for adj in graph[node]:
            if adj not in visited:
                visited.add(adj)
                cnt += 1
                stack.append(adj)
    return cnt


def main():
    N, M = map(int, input().split())

    graph = {node: [] for node in range(1, N+1)}
    rev_graph = {node: [] for node in range(1, N+1)}

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        rev_graph[b].append(a)

    is_fixed = 0

    for node in range(1, N+1):
        front = dfs(node, rev_graph)
        back = dfs(node, graph)

        # 내 앞에 있는 놈 + 내 뒤에 있는 놈 = 전체 학생 수 - 1 => 순서가 확정됨
        if front + back == N-1:
            is_fixed += 1

    print(is_fixed)


if __name__ == "__main__":
    main()
