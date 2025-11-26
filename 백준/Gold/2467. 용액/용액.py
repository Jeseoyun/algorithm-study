INF = float('inf')


def main():
    N = int(input())
    liquid_list = list(map(int, input().split()))

    left = 0
    right = N-1
    best_fit = [INF, INF, INF]  # 혼합액, 알칼리, 산성

    while left < right:
        val = liquid_list[left] + liquid_list[right]
        # print((left, right), ":", val)

        if abs(val) <= best_fit[0]:
            best_fit = [abs(val), liquid_list[left], liquid_list[right]]

        if val > 0:
            right -= 1
        elif val < 0:
            left += 1
        else:
            # val == 0 이면 더 이상 갱신할 필요 없음(이미 최적)
            break

    print(best_fit[1], best_fit[2])


if __name__ == "__main__":
    main()