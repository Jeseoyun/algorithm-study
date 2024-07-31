'''DFS 풀이 - 시간 초과 오류'''
# def select_candy(arr, k, idx, comb, selected):
#     if len(comb) == k:
#         selected.append(comb[-1]-comb[0])
#         return
#
#     if idx == len(arr):
#         return
#
#     # 현재 요소를 선택하는 경우
#     select_candy(arr, k, idx+1, comb+[arr[idx]], selected)
#     # 현재 요소를 선택하지 않는 경우
#     select_candy(arr, k, idx+1, comb, selected)
#
#
# def main():
#     T = int(input())
#
#     for test_case in range(1, T + 1):
#         N, K = map(int, input().split())
#         candy = list(map(int, input().split()))
#
#         selected = []
#         candy.sort()
#         select_candy(candy, K, 0, [], selected)
#
#         # diff = [max(comb)-min(comb) for comb in selected]
#
#         print(f"#{test_case} {min(selected)}")
#
#
# if __name__ == "__main__":
#     main()


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
