INF = float('inf')

## 1트: 부분합 배열 만들어서 체크
# def main():
#     N, S = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     part_sum = [0]*N
#     part_sum[0] = arr[0]
#     for i in range(1, N):
#         part_sum[i] = part_sum[i-1] + arr[i]
#
#     # print(part_sum)
#
#     min_len = INF
#     for i in range(N):
#         for j in range(i, N):
#             if i == 0 and part_sum[j] >= S:
#                 min_len = min(min_len, j+1)
#                 break
#             elif i != 0 and part_sum[j] - part_sum[i-1] >= S:
#                 min_len = min(min_len, j+1-i)
#                 break
#                 print(i, j, part_sum[j], part_sum[i], j+1-i)
#
#     print(min_len if min_len != INF else 0)

## 2트: 계속 누적합 연산하면서 체크
# def main():
#     N, S = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     min_len = INF
#     for i in range(N):
#         temp = 0
#
#         if arr[i] >= S:
#             min_len = 1
#             break
#
#         for j in range(i, N):
#             temp += arr[j]
#             temp_len = j-i+1
#
#             if temp < S:
#                 # print("더하기", i, j, temp)
#                 continue
#             if temp_len < min_len:
#                 min_len = temp_len
#             # min_len = min(min_len, j-i+1)
#             # print("넘었다!", i, j, temp, min_len)
#             break
#
#     print(min_len if min_len != INF else 0)


# 3트(답 확인): 투포인터 사용
def main():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    left, right = 0, 0
    part_sum = arr[0]
    min_len = INF

    while left <=  right:
        # print(f"left: {left}, right: {right}, part_sum: {part_sum}")

        # 현재까지 부분합이 S보다 작으면 right를 늘려서 값을 키운다
        if part_sum < S:
            right += 1
            if right >= N:
                # print(f"right: {right}, 동작그만")
                break
            part_sum += arr[right]

        # 현재까지 부분합이 S보다 같거나 크면 left를 늘려서 길이를 줄여본다
        else:
            min_len = min(min_len, right-left+1)
            part_sum -= arr[left]
            left += 1

    print(min_len if min_len != INF else 0)


if __name__ == "__main__":
    main()