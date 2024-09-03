from collections import deque


def bfs(grid, N, M):
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[-1]*M for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if grid[i][j] == "W":
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if visited[nx][ny] != -1:
                continue
            
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

    total_move_cnt = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == "L":
                total_move_cnt += visited[i][j]

    return total_move_cnt


def main():
    T = int(input())
    
    for test_case in range(1, T+1):
        N, M = map(int, input().split())
        grid = [list(input()) for _ in range(N)]

        result = bfs(grid, N, M)

        print(f"#{test_case} {result}")


if __name__ == "__main__":
    main()