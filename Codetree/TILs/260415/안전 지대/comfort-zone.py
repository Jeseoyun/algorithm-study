dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]


def print_board(board):
    for arr in board:
        for elem in arr:
            print(elem, end=" ")
        print()
    print()


def dfs(grid, visited, k, N, M, x, y):
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny]:
            continue
        if grid[nx][ny] <= k:
            continue

        visited[nx][ny] = 1
        dfs(grid, visited, k, N, M, nx, ny)


def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 최대, 최소 k 값 찾기
    min_k, max_k = float('inf'), 0
    for i in range(N):
        sorted_i = sorted(grid[i])
        min_k = min(min_k, sorted_i[0])
        max_k = max(max_k, sorted_i[-1])
    # print(min_k, max_k)

    best_safe_area = (0, 0)
    for k in range(min_k, max_k+1):
        # print(f"====={k}=====")
        visited = [[0]*M for _ in range(N)]
        safe_area = 0

        for i in range(N):
            for j in range(M):
                if grid[i][j] <= k:  # 물에 잠긴 구역
                    continue
                if visited[i][j]:  # 이미 영역에 속함
                    continue

                visited[i][j] = 1
                dfs(grid, visited, k, N, M, i, j)
                safe_area += 1
        if safe_area > best_safe_area[1]:
            best_safe_area = (k, safe_area)
        # print(f"safe_area: {safe_area}")
        # print_board(visited)

    print(*best_safe_area, sep=" ")


if __name__ == "__main__":
    main()
