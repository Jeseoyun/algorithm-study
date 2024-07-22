def harvest(field, n):
    mid = n//2
    total_sum = 0

    for i in range(n):
        for j in range(n):
            if abs(mid-i) + abs(mid-j) <= mid:
                total_sum += field[i][j]

    return total_sum


def main():
    t = int(input())

    for test_case in range(1, t+1):
        n = int(input())
        field = [list(map(int, list(input()))) for _ in range(n)]

        result = harvest(field, n)

        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()
