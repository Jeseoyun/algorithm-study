def main():
    MOD = 1000000007
    N = int(input())

    dp = [0] * (N + 1)

    # 초기값
    dp[0] = 1
    if N >= 1:
        dp[1] = 2

    for i in range(2, N + 1):
        # 2x1 남는 경우 2가지
        # 2x2 남는 경우 새로 생기는 3가지
        dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % MOD

        # 2x3 이상 남는 삐진 형태들 누적
        for j in range(i-2):  # 0 ~ i-3까지 2개씩 계속 발생
            dp[i] = (dp[i] + dp[j] * 2) % MOD

    print(dp[N])


if __name__ == "__main__":
    main()