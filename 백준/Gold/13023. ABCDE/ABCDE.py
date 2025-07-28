def dfs(depth, curr, graph, visited):
    # print(depth, curr)
    if depth == 4:
        # print("gotcha!")
        return True

    visited.add(curr)

    for neighbor in graph[curr]:
        if neighbor in visited:
            continue
        if dfs(depth+1, neighbor, graph, visited):
            return True

    visited.remove(curr)

    # print("그냥 종료!")


def main():
    N, M = map(int, input().split())
    graph = {i: [] for i in range(N)}

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    is_exist = False
    for node in graph:
        # print("시작노드:",node)
        if is_exist:
            break
        visited = set()
        is_exist = dfs(0, node, graph, visited)

    print(1 if is_exist else 0)


if __name__ == "__main__":
    main()