def main():
    n = int(input())
    dancers = set()
    dancers.add("ChongChong")

    for _ in range(n):
        a, b = input().strip().split()

        if (a in dancers) or (b in dancers):
            dancers.add(a)
            dancers.add(b)

    print(len(dancers))

if __name__ == "__main__":
    main()