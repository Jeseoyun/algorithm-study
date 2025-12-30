import math


def get_additional_sa(gap, X):
    need = 0
    for g in gap:
        need += math.ceil(g/X) - 1
    return need


def main():
    N, M, L = map(int, input().split())
    service_area = list(map(int, input().split()))

    service_area.sort()
    service_area.insert(0, 0)
    service_area.insert(N+1, L)

    gap = []
    for i in range(N+1):
        gap.append(service_area[i+1]-service_area[i])

    start = 1  # 휴게소 사이 최소 거리
    end = L-1  # 휴게소 사이 최대 거리

    best = float('inf')
    while start <= end:
        mid = (start + end) // 2  # 비교 대상(휴게소 사이 거리)
        
        need = get_additional_sa(gap, mid)
        if need <= M:
            end = mid - 1
            best = min(best, mid)
        else:
            start = mid + 1

    print(best)


if __name__ == "__main__":
    main()