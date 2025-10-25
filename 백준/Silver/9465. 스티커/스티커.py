def main():
    T = int(input())

    for _ in range(T):
        n = int(input())
        sticker = [list(map(int, input().split())) for _ in range(2)]
        dp = [[0]*3 for _ in range(n)]

        # 초기값
        dp[0][0] = 0
        dp[0][1] = sticker[0][0]  # 위에꺼 떼어냄
        dp[0][2] = sticker[1][0]  # 밑에꺼 떼어냄

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])  # 아무것도 안고를 경우 최대 점수
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + sticker[0][i]  # i열에서 윗줄 스티커 골랐을 때 최대 점수
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + sticker[1][i]  # i열에서 아랫줄 스티커 골랐을 때 최대 점수

        print(max(dp[n-1]))


if __name__ == "__main__":
    main()