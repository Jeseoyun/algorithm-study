N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)


dp = [0]*(N+1)  # N개 살 때 최댓값
dp[0] = P[0]
for i in range(1, N+1):
    for j in range(i+1):
        dp[i] = max(dp[i], dp[i-j]+P[j])
        # print(i, j, dp)
print(dp[-1])