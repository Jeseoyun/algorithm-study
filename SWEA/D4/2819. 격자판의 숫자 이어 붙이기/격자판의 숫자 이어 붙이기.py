'''
def search_dfs(grid, i, j, visited, visited_set, depth=0):
    if depth >= 7:
        if len(visited) == 7 and (visited not in visited_set):
            visited_set.add(visited)
        # print("종료1")
        return

    visited += grid[i][j]
    # print(f"grid[{i}][{j}]: {grid[i][j]}, visited: {visited}, depth: {depth} ")

    if i < len(grid)-1:
        search_dfs(grid, i+1, j, visited, visited_set, depth+1)  # 아래쪽 이동
    if i > 0:
        search_dfs(grid, i-1, j, visited, visited_set, depth+1)  # 위로 이동
    if j < len(grid[0])-1:
        search_dfs(grid, i, j+1, visited, visited_set, depth+1)  # 오른쪽 이동
    if j > 0:
        search_dfs(grid, i, j-1, visited, visited_set, depth+1)  # 왼쪽 이동
    # print("종료2")


def main():
    import sys
    sys.stdin = open("input.txt", "r")

    T = int(input())
    N = 4

    for test_case in range(1, T+1):
        grid = [input().split() for _ in range(N)]

        visited_set = set()
        for i in range(N):
            for j in range(N):
                search_dfs(grid, i, j, "", visited_set)
        print(f"#{test_case} {len(visited_set)}")


if __name__ == "__main__":
    main()

'''


def search_dfs(grid, i, j, visited, visited_set, depth=0):
    if depth == 7:
        visited_set.add(tuple(visited))
        return

    visited.append(grid[i][j])

    if i < len(grid) - 1:
        search_dfs(grid, i + 1, j, visited, visited_set, depth + 1)  # 아래로 이동
    if i > 0:
        search_dfs(grid, i - 1, j, visited, visited_set, depth + 1)  # 위로 이동
    if j < len(grid[0]) - 1:
        search_dfs(grid, i, j + 1, visited, visited_set, depth + 1)  # 오른쪽 이동
    if j > 0:
        search_dfs(grid, i, j - 1, visited, visited_set, depth + 1)  # 왼쪽 이동

    visited.pop()


def main():
    T = int(input())
    N = 4

    for test_case in range(1, T + 1):
        grid = [input().split() for _ in range(N)]

        visited_set = set()
        for i in range(N):
            for j in range(N):
                search_dfs(grid, i, j, [], visited_set)
        print(f"#{test_case} {len(visited_set)}")


if __name__ == "__main__":
    main()
