def main():
    N = int(input())
    nums = list(map(int, input().split()))

    dp = [1]*N  # i번째 원소 선택 시 최대 길이
    prev = [-1]*N  # 이전에 저장된 값 정보

    for i in range(1, N):
        for j in range(i):
            # print(i,j, nums[i], nums[j])
            # i번째 원소보다 더 작은값이 있는지 탐색
            if nums[j] < nums[i]:
                if dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
                    prev[i] = j
            # print("dp:",dp)
            # print("prev:",prev)

    res = []
    cur = dp.index(max(dp))
    while True:
        res.append(nums[cur])

        if prev[cur] == -1:
            break

        cur = prev[cur]

    print(max(dp))
    print(" ".join(map(str, res[::-1])))


if __name__ == "__main__":
    main()