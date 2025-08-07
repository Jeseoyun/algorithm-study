def main():
    N, K = map(int, input().split())
    item = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [0]*(K+1)

    for w, v in item:
        for weight in range(K, w-1, -1):
            dp[weight] = max(dp[weight], dp[weight-w] + v)

    print(max(dp))


if __name__ == "__main__":
    main()