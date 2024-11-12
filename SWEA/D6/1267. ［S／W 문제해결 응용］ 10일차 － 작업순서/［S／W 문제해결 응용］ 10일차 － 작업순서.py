from collections import defaultdict, deque


def main():
    T = 10

    for test_case in range(1, T+1):
        V, E = map(int, input().split())
        edges = list(map(int, input().split()))

        # initialize
        graph = defaultdict(list)
        in_degree = {node: 0 for node in range(1, V + 1)}  # 각 노드의 진입 차수
        for i in range(0, len(edges), 2):
            graph[edges[i]].append(edges[i+1])
            in_degree[edges[i+1]] += 1

        # 진입 차수가 0인 정점을 큐에 삽입
        queue = deque()
        for v in in_degree.keys():
            if in_degree[v] == 0:
                queue.append(v)

        result = []
        visited = 0

        while queue:
            curr = queue.popleft()
            result.append(curr)
            visited += 1

            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

            del graph[curr]

        print(f"#{test_case} {' '.join(str(r) for r in result)}")


if __name__ == "__main__":
    main()