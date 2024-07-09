def func(n, k, an):
    sorted_an = sorted(an)

    min_diff = 10**9
    for i in range(n-k+1):
        diff = sorted_an[i+k-1] - sorted_an[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff


if __name__ == "__main__":
    T = int(input())

    for test_case in range(T):
        n, k = map(int, input().split())  # 주머니 개수, 나눠 줄 주머니 개수
        an = list(map(int, input().split()))

        result = func(n, k, an)

        print(f"#{test_case+1} {result}")
