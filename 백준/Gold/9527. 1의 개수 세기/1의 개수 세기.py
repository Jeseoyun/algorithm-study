def get_one_count(n):
    if n < 0:
        return 0

    total = 0
    while n > 0:
        p = 1  # n보다 작거나 같은 가장 큰 2의 거듭제곱수
        while p*2 <= n:
            p *= 2

        k = 0  # p = 2^k, k=log2(p), 즉 k: p가 2의 몇 승인지
        temp = p
        while temp > 1:
            temp //= 2
            k += 1
        # 0 ~ p-1 구간에서 1 개수: 무조건 전체 개수의 절반이 1
        total += k * (p//2)

        # p ~ n 구간에서는 최상위 비트가 모두 켜져있음
        total += (n-p+1)

        # 최상위 비트 떼고 남은 값으로 축소
        n -= p

    return total


def main():
    A, B = map(int, input().split())

    print(get_one_count(B)-get_one_count(A-1))


# B의 크기가 10^16 -> 메모리 초과
# def main():
#     A, B = map(int, input().split())
#
#     memo = [0]*(B+1)
#     # initialize
#     temp = 1
#     while temp <= B+1:
#         memo[temp] = 1
#         temp *= 2
#
#     recent_idx = 0
#     for i in range(B+1):
#         if memo[i] == 1:
#             recent_idx = i
#             continue
#         memo[i] = memo[recent_idx] + memo[i-recent_idx]
#
#     print(sum(memo[A:B+1]))


if __name__ == "__main__":
    main()