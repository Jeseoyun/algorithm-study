from collections import deque


def bfs(grid, N, M, sx, sy):
    visited = [[0]*M for _ in range(N)]
    visited[sx][sy] = 1
    queue = deque([(sx, sy, 1)])

    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    last_nx, last_ny = 0, 0
    curr_max_len = 0

    while queue:
        x, y, l = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny]:
                continue

            if grid[nx][ny] == 0:
                continue

            visited[nx][ny] = 1
            queue.append((nx, ny, l+1))

            if curr_max_len < l+1:
                last_nx, last_ny = nx, ny
                curr_max_len = l+1

    return last_nx, last_ny, curr_max_len


def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0
    password = 0
    for sx in range(N):
        for sy in range(M):
            if A[sx][sy] == 0:
                continue

            # print("sx, sy", (sx, sy))
            ex, ey, ml = bfs(A, N, M, sx, sy)
            # print(ex, ey, ml)
            if max_len < ml:
                max_len = ml
                password = A[sx][sy] + A[ex][ey]
            elif max_len == ml:
                password = max(password, A[sx][sy] + A[ex][ey])

    print(password)


if __name__ =="__main__":
    main()