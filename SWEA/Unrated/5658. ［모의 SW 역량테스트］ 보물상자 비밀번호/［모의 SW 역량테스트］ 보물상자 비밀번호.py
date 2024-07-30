def max_hex_decimal(hex_nums):
    dec = set()
    for _ in range(N-1):  # rotate를 진행할 횟수
        num_split = [hex_nums[i:i+(N//4)] for i in range(0, len(hex_nums), (N//4))]

        for num in num_split:
            dec.add(int(''.join(num), 16))

        hex_nums.insert(0, hex_nums.pop(-1))  # rotate

    sorted_dec = sorted(list(dec), reverse=True)
    return sorted_dec[K-1]


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    hex_nums = list(input())

    result = max_hex_decimal(hex_nums)

    print(f"#{test_case} {result}")