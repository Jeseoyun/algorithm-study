def main():
    N = int(input())

    initial = [0, 2, 7, 22]
    if N < 4:
        print(initial[N])
        return
    else:
        dp = [0]*(N+1)

        for i in range(4):
            dp[i] = initial[i]

    for i in range(4, N+1):
        dp[i] = dp[i-1]*2 + dp[i-2]*3 + dp[i-3]*2
        # print(dp)

    print(dp[N])


if __name__ == "__main__":
    main()
