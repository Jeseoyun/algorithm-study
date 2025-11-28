INF = float('inf')


def main():
    N = int(input())
    liquid_list = list(map(int, input().split()))
    liquid_list.sort()

    best_fit = [INF, INF, INF, INF]  # 혼합액 값, 첫 번째 용액, 두 번째 용액, 세 번째 용액
    for fst in range(N-2):
        sec = fst+1
        thrd = N-1

        while sec < thrd:
            val = liquid_list[fst] + liquid_list[sec] + liquid_list[thrd]

            if abs(val) < best_fit[0]:  # 최적값 갱신
                best_fit = [abs(val), liquid_list[fst], liquid_list[sec], liquid_list[thrd]]

            # 0에 가깝게 만들어야 함
            if val < 0:
                sec += 1  # 음수일 경우 더 큰 값을 더해줘야 함
            elif val > 0:
                thrd -= 1  # 양수일 경우 더 작은 값을 더해줘야 함
            else:
                break  # 0일 경우 바로 종료

        if best_fit[0] == 0:
            break

    print(*best_fit[1:])


if __name__ == "__main__":
    main()