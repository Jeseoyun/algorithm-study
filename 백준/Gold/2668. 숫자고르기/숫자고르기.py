def dfs(start, curr, numbs, visited, path):
    if visited[curr]:
        if curr == start:
            return path
        else:
            return []

    visited[curr] = True
    path.append(curr)
    return dfs(start, numbs[curr], numbs, visited, path)


def main():
    N = int(input())
    numbs = {i: int(input()) for i in range(1, N + 1)}

    result = []

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        path = dfs(i, i, numbs, visited, [])
        if path:
            result.extend(path)

    result = sorted(set(result))
    print(len(result))
    for num in result:
        print(num)


if __name__ == "__main__":
    main()