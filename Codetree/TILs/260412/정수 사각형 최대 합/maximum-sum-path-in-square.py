dxy = [(1, 0), (0, 1)]  # 밑, 오른쪽으로만 이동


def dfs(x, y):
    if (x, y) == (n-1, n-1):
        return grid[x][y]

    if dp[x][y] != -1:
        return dp[x][y]

    max_val = 0

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        max_val = max(max_val, dfs(nx, ny))

    dp[x][y] = grid[x][y] + max_val
    return dp[x][y]


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(n)]

print(dfs(0, 0))