def main():
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    result = 0

    for idx in range(N):
        target = numbers[idx]
        left, right = 0, N-1

        while left < right:
            if left == idx:
                left += 1
                continue
            if right == idx:
                right -= 1
                continue

            s = numbers[left] + numbers[right]

            if s == target:
                result += 1
                break
            elif s < target:
                left += 1
            else:
                right -= 1

    print(result)


if __name__ == "__main__":
    main()