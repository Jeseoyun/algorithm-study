# 고객 수 >= C를 만드는 최소 비용
# dp[x] = 고객 x명을 확보하는 데 필요한 최소 비용


INF = float('inf')


def main():
    C, N = map(int, input().split())  # 최소 홍보 인원, 도시 수
    city = [tuple(map(int, input().split())) for _ in range(N)]  # 비용, 고객 수

    max_people = max(c[1] for c in city)
    dp = [INF]*(C+max_people+1)
    dp[0] = 0

    for (cost, people) in city:
        for x in range(people, C+max_people+1):
            dp[x] = min(dp[x], dp[x-people] + cost)

    print(min(dp[C:]))


if __name__ == "__main__":
    main()