from collections import deque


dxy = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def bfs(matrix, N, M):
    queue = deque([(0, 0, 0)])  # x, y, used

    # visited[x][y][used]: used=0(벽 안부숨), used=1(벽 부숨)
    visited = [[[-1]*2 for _ in range(M)] for __ in range(N)]
    visited[0][0][0] = 1

    while queue:
        x, y, used = queue.popleft()

        if (x, y) == (N-1, M-1):
            return visited[x][y][used]

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 빈칸으로 이동
            if matrix[nx][ny] == '0':
                if visited[nx][ny][used] != -1:
                    continue
                visited[nx][ny][used] = visited[x][y][used] + 1
                queue.append((nx, ny, used))

            # 벽 부수고 이동
            else:
                if not used:
                    if visited[nx][ny][1] != -1:
                        continue
                    visited[nx][ny][1] = visited[x][y][used] + 1
                    queue.append((nx, ny, 1))

    return -1


def main():
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    min_dist = bfs(matrix, N, M)
    print(min_dist)


if __name__ == "__main__":
    main()