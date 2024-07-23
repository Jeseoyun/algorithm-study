# def bit_reader(n, m):
#     binary_num = bin(m)[2:]  # '0bXXXX'에서 '0b' 제거
#     # print(m, binary_num)
#     for i in range(len(binary_num)):
#         # print(n, i, binary_num[len(binary_num)-1-i])
#         if binary_num[len(binary_num)-1-i] == '0':  # 0이 나오면 OFF
#             return "OFF"
#         if i >= n-1:  # early return
#             break
#     return "ON"

def bit_reader(n, m):
    binary_num = bin(m)[2:]
    if n != sum(map(int, list(binary_num)[::-1][:n])):
        return "OFF"
    else:
        return "ON"


def main():
    TC = int(input())

    for test_case in range(1, TC+1):
        N, M = map(int, input().split())
        result = bit_reader(N, M)
        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()
