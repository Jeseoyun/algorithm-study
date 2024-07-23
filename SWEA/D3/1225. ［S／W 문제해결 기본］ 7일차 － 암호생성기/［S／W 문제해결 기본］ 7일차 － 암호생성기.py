from collections import deque


def cycle(code):
    for i in range(1, 6):  # 5번
        target = code.popleft()
        new_value = target-i if target-i > 0 else 0
        code.append(new_value)

        if new_value == 0:
            break


def main():
    T = 10

    for _ in range(1, T+1):
        test_case = int(input())
        code = deque(map(int, input().split()))

        while all(n > 0 for n in code):
            cycle(code)

        result = " ".join(map(str, code))

        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()
