max_number = 0


def dfs(number, max_change_cnt, check, depth=0):
    global max_number
    if depth == max_change_cnt:
        res_num = sum(int(n)*(10**(len(number)-i-1)) for i, n in enumerate(number))
        max_number = max(max_number, res_num)
        return

    for i in range(len(number)-1):
        for j in range(i+1, len(number)):
            number[i], number[j] = number[j], number[i]
            new_number = "".join(number)
            if (depth, new_number) not in check:
                dfs(number, max_change_cnt, check, depth+1)
                check.add((depth, new_number))
            number[i], number[j] = number[j], number[i]


def main():
    T = int(input())

    for test_case in range(1, T+1):
        global max_number
        max_number = 0

        number, max_change_cnt = input().split()
        number = list(number)
        max_change_cnt = int(max_change_cnt)

        check = set()
        dfs(number, max_change_cnt, check)

        print(f"#{test_case} {max_number}")


if __name__ == "__main__":
    main()