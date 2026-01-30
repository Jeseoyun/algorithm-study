import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    h = [int(input()) for _ in range(N)]
    h.append(0)

    stack = []
    max_area = 0

    for i in range(N + 1):
        while stack and h[stack[-1]] > h[i]:
            idx = stack.pop()
            height = h[idx]

            left = stack[-1] if stack else -1
            width = i - left - 1
            area = height * width

            if area > max_area:
                max_area = area

        stack.append(i)

    print(max_area)


if __name__ == "__main__":
    main()
