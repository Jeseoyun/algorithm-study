def main():
    N = int(input())

    a, b = 1, 2

    for _ in range(3, N+1):
        a, b = b, (a + b) % 15746

    print(b if N > 1 else a)


if __name__ =="__main__":
    main()