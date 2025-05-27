def main():
    N = int(input())
    stair = [int(input()) for _ in range(N)]

    if N == 1:
        print(stair[0])
        return
    elif N == 2:
        print(stair[0] + stair[1])
        return

    dp = [0] * N
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])  # 2칸 vs. 1칸+1칸

    for i in range(3, N):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])  # 직전으로부터 2칸 vs. 직전보다 1칸 전에서 1칸+1칸

    print(dp[N-1])


if __name__ == "__main__":
    main()