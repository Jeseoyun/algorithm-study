from collections import defaultdict, deque


def main():
    N, M = map(int, input().split())
    height_order = defaultdict(list)
    in_degree = {i+1: 0 for i in range(N)}

    for _ in range(M):
        a, b = map(int, input().split())
        height_order[a].append(b)
        in_degree[b] += 1

    queue = deque()
    for node in range(1, N+1):
        if in_degree[node] == 0:
            queue.append(node)

    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in height_order[current]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    print(" ".join(str(s) for s in result))


if __name__ == "__main__":
    main()