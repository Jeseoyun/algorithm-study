from collections import Counter


def get_divisor(n):
    divisor = set()
    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            divisor.add(i)
            if (i**2) != n:
                divisor.add(n//i)
    return divisor


def main():
    N = int(input().rstrip())
    numbers = [int(input().rstrip()) for _ in range(N)]

    freq = Counter(numbers)
    divisor_map = {n: get_divisor(n) for n in set(numbers)}

    for i in range(N):
        toktok = 0
        curr = numbers[i]

        for d in divisor_map[curr]:
            toktok += freq[d]

        toktok -= 1
        print(toktok)


if __name__ == "__main__":
    main()