def main():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0]*N for _ in range(N)]
    dp[0][N-1] = grid[0][N-1]

    for j in range(N-2, -1, -1):
        dp[0][j] = dp[0][j+1] + grid[0][j]

    for i in range(1, N):
        dp[i][N-1] = dp[i-1][N-1] + grid[i][N-1]
        for j in range(N-2, -1, -1):
            dp[i][j] += min(dp[i-1][j], dp[i][j+1]) + grid[i][j]

    print(dp[N-1][0])


if __name__ == "__main__":
    main()