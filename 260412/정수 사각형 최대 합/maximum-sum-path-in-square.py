dxy = [(1, 0), (0, 1)]  # 밑, 오른쪽으로만 이동


def dfs(x, y):
    if (x, y) == (n-1, n-1):
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        visited[nx][ny] = max(visited[nx][ny], visited[x][y] + grid[nx][ny])
        dfs(nx, ny)

    return


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
visited[0][0] = grid[0][0]

dfs(0, 0)

print(visited[n-1][n-1])
