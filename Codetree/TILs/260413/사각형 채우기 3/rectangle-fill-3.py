MOD = 1000000007


def main():
    N = int(input())

    dp = [0]*(N+1)
    extra = [0]*(N+1)

    dp[0] = 1
    if N >= 1:
        dp[1] = 2
        extra[1] = 1

    for i in range(2, N+1):
        extra[i] = (dp[i-1] + extra[i-1]) % MOD
        dp[i] = (2*dp[i-1] + dp[i-2] + 2*extra[i-1]) % MOD
        # print(dp)

    print(dp[N])


if __name__ == "__main__":
    main()
