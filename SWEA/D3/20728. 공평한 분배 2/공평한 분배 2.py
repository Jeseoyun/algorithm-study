def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N, K = map(int, input().split())
        candy_bundle = list(map(int, input().split()))

        # 정렬하고
        candy_bundle.sort()
        # 연속된 놈들의 조합에서 최대, 최소 구한다
        min_diff = float('inf')
        for i in range(len(candy_bundle)-K+1):
            candy = candy_bundle[i:i+K]
            min_diff = min(min_diff, candy[-1]-candy[0])

        print(f"#{test_case} {min_diff}")


if __name__ == "__main__":
    main()