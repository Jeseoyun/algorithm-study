def main():
    N = int(input())

    dp = [[0]*2 for _ in range(N)]  # 0일 경우, 1일 경우

    dp[0][0] = 0  # 첫 번째 자리 수가 0인 경우 - 불가
    dp[0][1] = 1

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]  # 0, 1 가능
        dp[i][1] = dp[i-1][0]  # 0만 가능

    print(sum(dp[N-1]))


if __name__ == "__main__":
    main()