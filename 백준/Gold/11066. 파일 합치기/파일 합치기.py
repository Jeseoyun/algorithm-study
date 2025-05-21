INF = float('inf')


def main():
    T = int(input())

    for _ in range(T):
        K = int(input())
        files = list(map(int, input().split()))

        # prefix_sum[i] = files[0]부터 files[i-1] 까지의 합
        prefix_sum = [0] * (K+1)
        for i in range(K):
            prefix_sum[i+1] = prefix_sum[i] + files[i]

        dp = [[0]*K for _ in range(K)]
        for length in range(2, K+1):  # 2~K개까지 구간
            for start in range(K-length+1):
                end = start + length - 1
                dp[start][end] = INF

                for mid in range(start, end):
                    merge_cost = prefix_sum[end+1] - prefix_sum[start]
                    cost = dp[start][mid] + dp[mid+1][end] + merge_cost

                    dp[start][end] = min(dp[start][end], cost)
                    # print(start, end, mid)
                    # print(dp)

        print(dp[0][K-1])


if __name__ == "__main__":
    main()