from collections import deque

INF = float('inf')


def sort_game(arr, n, k, idx):
    queue = deque([(arr[:], 0)])
    target = sorted(arr)
    visited = set()

    while queue:
        # print(queue)
        curr, cnt = queue.popleft()

        if curr == target:
            return cnt

        if tuple(curr) in visited:
            continue

        visited.add(tuple(curr))

        for i in range(n-k+1):
            part_sorted = curr[:]
            part_sorted[i:i+k] = reversed(curr[i:i+k])
            queue.append((part_sorted, cnt+1))

    return -1


def main():
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))

    min_cnt = INF
    for idx in range(0, N-K+1):
        cnt = sort_game(arr, N, K, 0)
        min_cnt = min(cnt, min_cnt) if cnt != -1 else min_cnt

    print(min_cnt if min_cnt!=INF else -1)


if __name__ == "__main__":
    main()