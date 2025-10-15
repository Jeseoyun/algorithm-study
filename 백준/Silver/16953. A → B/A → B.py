from collections import deque


def main():
    A, B = map(int, input().split())

    queue = deque([(A, 1)])

    while queue:
        curr, depth = queue.popleft()

        for new in [curr*2, curr*10+1]:
            if new > 10**9:
                continue

            if new == B:
                print(depth+1)
                return

            queue.append((new, depth+1))

    print(-1)
    return

if __name__ == "__main__":
    main()