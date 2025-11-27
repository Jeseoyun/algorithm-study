INF = float('inf')


def main():
    N = int(input())
    liquid_list = list(map(int, input().split()))

    # 이분탐색 위한 정렬
    liquid_list.sort()

    left = 0
    right = N-1
    best_fit = [INF, INF, INF]

    while left < right:
        val = liquid_list[left] + liquid_list[right]

        if abs(val) < best_fit[0]:
            best_fit = [abs(val), liquid_list[left], liquid_list[right]]

        if val < 0:
            left += 1
        elif val > 0:
            right -= 1
        else:
            best_fit = [abs(val), liquid_list[left], liquid_list[right]]
            break


    print(best_fit[1], best_fit[2])


if __name__ == "__main__":
    main()