INF = float('inf')


def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dp = [[-INF]*M for _ in range(N)]

    # 1열 초기화
    dp[0][0] = grid[0][0]
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, N):
        left = [-INF] * M
        right = [-INF] * M

        # 왼 -> 오
        left[0] = dp[i-1][0] + grid[i][0]
        for j in range(1, M):
            left[j] = max(dp[i-1][j], left[j-1]) + grid[i][j]

        # 오 -> 왼
        right[M-1] = dp[i-1][M-1] + grid[i][M-1]
        for j in range(M-2, -1, -1):
            right[j] = max(dp[i-1][j], right[j+1]) + grid[i][j]

        # 현재 행 갱신
        for j in range(M):
            dp[i][j] = max(left[j], right[j])

    print(dp[N-1][M-1])


if __name__ == "__main__":
    main()