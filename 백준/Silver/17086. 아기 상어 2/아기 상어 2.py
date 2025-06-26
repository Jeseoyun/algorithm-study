from collections import deque


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 인접 8방향 이동 가능


def bfs(space, N, M, sx, sy):
    if space[sx][sy] == 1:
        return 0

    queue = deque([(sx, sy, 0)])
    visited = [[0]*M for _ in range(N)]
    visited[sx][sy] = 1

    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny] == 1:
                continue

            if space[nx][ny] == 1:
                return dist + 1

            queue.append((nx, ny, dist+1))
            visited[nx][ny] = 1

    return 0


def main():
    N, M = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(N)]

    max_dist = 0
    for i in range(N):
        for j in range(M):
            dist = bfs(space, N, M, i, j)
            max_dist = max(max_dist, dist)

    print(max_dist)


if __name__ == "__main__":
    main()