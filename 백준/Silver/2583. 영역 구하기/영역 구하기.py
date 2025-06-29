import copy
from collections import deque


def print_board(grid):
    for lst in grid:
        for elem in lst:
            print(elem, end=" ")
        print()


def bfs(grid, N, M, visited, sx, sy):
    visited[sx][sy] = 1
    queue = deque([(sx, sy)])

    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    area = 1

    while queue:
        # print(queue)
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny]:
                continue

            if grid[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            queue.append((nx, ny))
            area += 1

    return area


def main():
    M, N, K = map(int, input().split())  # max_y, max_x
    grid = [[0]*M for _ in range(N)]

    for _ in range(K):
        lb_x, lb_y, rt_x, rt_y = map(int, input().split())

        # 1. 색칠되는 영역 구하기
        for i in range(lb_x, rt_x):
            for j in range(lb_y, rt_y):
                grid[i][j] = 1

    # print_board(grid)

    # 2. 각 영역의 넓이 구하기
    area = []
    visited = copy.deepcopy(grid)
    for sx in range(N):
        for sy in range(M):
            # print("시작", sx, sy)
            if grid[sx][sy] == 1:
                continue
            if visited[sx][sy]:
                continue
            area.append(bfs(grid, N, M, visited, sx, sy))

    print(len(area))  # 영역 개수
    print(" ".join(map(str, sorted(area))))  # 각 영역 넓이(오름차순)


if __name__ == "__main__":
    main()