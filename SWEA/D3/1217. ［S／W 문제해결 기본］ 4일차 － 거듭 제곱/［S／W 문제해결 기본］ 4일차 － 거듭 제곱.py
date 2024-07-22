def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)


def main():
    n = 10  # test case 개수
    
    for _ in range(n):
        t = int(input())
        n, m = map(int, list(input().split()))

        result = power(n, m)

        print(f"#{t} {result}")


if __name__ == "__main__":
    main()
