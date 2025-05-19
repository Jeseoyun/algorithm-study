n = int(input())
box = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        # print(i, j)
        if box[j] < box[i]:
            dp[i] = max(dp[i], dp[j]+1)
            # print(dp)

print(max(dp))