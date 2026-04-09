def main():
    N = int(input())
    a, b = 1, 1

    if N <= 2:
        print(1)
        return

    for i in range(N-2):
        a, b = a+b, a
    
    print(a)


if __name__ == "__main__":
    main()