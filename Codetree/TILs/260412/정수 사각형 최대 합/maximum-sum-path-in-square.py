dxy = [(1, 0), (0, 1)]  # 밑, 오른쪽으로만 이동
max_sum = 0


def dfs(x, y, curr):
    global max_sum

    if (x, y) == (n-1, n-1):
        max_sum = max(max_sum, curr)
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny]:
            continue
        
        visited[nx][ny] = True
        dfs(nx, ny, curr+grid[nx][ny])
        visited[nx][ny] = False

    return


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]
visited[0][0] = True

dfs(0, 0, grid[0][0])

print(max_sum)
