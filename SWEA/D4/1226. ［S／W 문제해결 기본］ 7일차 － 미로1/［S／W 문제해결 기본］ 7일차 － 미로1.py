from collections import deque


def is_possible(maze, n, point):
    x, y = point
    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True  # 시작 지점 방문 체크

    queue = deque([[x, y]])

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 범위를 벗어난 지점
                continue

            if visited[nx][ny]:  # 이미 방문한 경우
                continue

            if maze[nx][ny] == 1:  # 벽(1)인 경우
                continue

            if maze[nx][ny] == 3:  # 도착지점(3)인 경우
                return 1  # 1: 도착 가능함을 반환


            visited[nx][ny] = True
            queue.append([nx, ny])

    return 0   # 0: 도착 불가능함을 반환


def main():
    T = 10
    N = 16

    for _ in range(T):
        test_case = int(input())
        maze = [list(map(int, input())) for _ in range(N)]

        start_idx = (0, 0)
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    start_idx = (i, j)

        result = is_possible(maze, N, start_idx)
        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()