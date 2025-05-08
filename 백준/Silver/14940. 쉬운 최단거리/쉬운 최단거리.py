from collections import deque

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_destination(grid, n, m):
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 2:
                return x, y
    return -1, -1


def main():
    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]

    # 1. 목표 지점 찾기
    sx, sy = find_destination(grid, n, m)

    # 2. 거리 탐색
    visited = [[-1 if grid[i][j] != 0 else 0 for j in range(m)] for i in range(n)]
    queue = deque([(sx, sy)])
    visited[sx][sy] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] != -1:
                continue
            if grid[nx][ny] == 0:
                continue

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

    print('\n'.join((' ').join(map(str, arr)) for arr in visited))


if __name__ == "__main__":
    main()