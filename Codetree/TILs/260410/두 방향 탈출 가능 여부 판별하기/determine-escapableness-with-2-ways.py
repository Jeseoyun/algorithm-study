dxy = [(1, 0), (0, 1)]  # 아래, 오른쪽


def print_board(grid):
    for arr in grid:
        for elem in arr:
            print(elem, end=" ")
        print()
    print()


def dfs(grid, visited, x, y, N, M):
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny]:
            continue
        if grid[nx][ny] == 0:
            continue

        if (nx, ny) == (N-1, M-1):
            visited[nx][ny] = 1
            return

        visited[nx][ny] = 1
        dfs(grid, visited, nx, ny, N, M)


def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    dfs(grid, visited, 0, 0, N, M)
    # print_board(visited)

    print(visited[N-1][M-1])


if __name__ == "__main__":
    main()