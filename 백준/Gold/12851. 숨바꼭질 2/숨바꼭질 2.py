from collections import deque

LIMIT = 100001
INF = float('inf')

def main():
    n, k = map(int, input().split())  # 시작점, 도착점

    # if n == k:
    #     print(0, 1, sep="\n")
    #     return

    queue = deque([n])
    visited = [INF for _ in range(LIMIT)]
    visited[n] = 0

    min_time = INF
    min_time_cnt = 0

    while queue:
        x = queue.popleft()

        if x == k:
            if min_time > visited[x]:
                min_time = visited[x]
                min_time_cnt = 1
            elif min_time == visited[x]:
                min_time_cnt += 1

        for nx in (x - 1, x + 1, 2 * x):
            if nx < 0 or nx >= LIMIT:
                continue
            if visited[nx] < visited[x] + 1:
                continue

            if visited[nx] >= visited[x] + 1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

    print(min_time)
    print(min_time_cnt)

if __name__ == "__main__":
    main()