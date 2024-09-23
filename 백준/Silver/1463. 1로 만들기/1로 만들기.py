N = int(input())

dp = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        dp[i] = 0
        continue
        
    if i == 2 or i == 3:
        dp[i] = 1
        continue

    cmp = []
    if i%3 == 0:
        cmp.append(dp[i//3] + 1)
    if i%2 == 0:
        cmp.append(dp[i//2] + 1)
    cmp.append(dp[i-1] + 1)

    dp[i] = min(cmp)

print(dp[-1])