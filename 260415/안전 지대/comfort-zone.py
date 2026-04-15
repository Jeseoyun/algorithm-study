from collections import deque

dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]


def bfs(grid, visited, k, N, M, x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if grid[nx][ny] <= k:
                continue

            visited[nx][ny] = 1
            queue.append((nx, ny))


def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_k = max(map(max, grid))

    best_k = 1
    best_safe_area = 0

    for k in range(1, max_k + 1):
        visited = [[0] * M for _ in range(N)]
        safe_area = 0

        for i in range(N):
            for j in range(M):
                if grid[i][j] <= k:
                    continue
                if visited[i][j]:
                    continue

                bfs(grid, visited, k, N, M, i, j)
                safe_area += 1

        if safe_area > best_safe_area:
            best_safe_area = safe_area
            best_k = k

    print(best_k, best_safe_area)


if __name__ == "__main__":
    main()