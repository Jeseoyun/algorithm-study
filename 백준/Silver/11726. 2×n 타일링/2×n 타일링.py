def main():
    n = int(input())
    dp = [0 for _ in range(n+1)]

    if n <= 2:
        print(n%10007)
        return

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    # print(dp)
    print(dp[n]%10007)


if __name__ =="__main__":
    main()