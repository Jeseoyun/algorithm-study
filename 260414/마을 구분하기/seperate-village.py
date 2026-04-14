dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]


def print_board(board):
    for arr in board:
        for elem in arr:
            print(elem, end=" ")
        print()
    print()


def dfs(grid, N, visited, x, y):
    cnt = 1

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny]:
            continue
        if grid[nx][ny] == 0:
            continue

        visited[nx][ny] = 1
        cnt += dfs(grid, N, visited, nx, ny)

    return cnt


def main():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    village = []
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if grid[i][j] == 0:
                continue

            visited[i][j] = 1
            cnt = dfs(grid, N, visited, i, j)
            village.append(cnt)

            # print("cnt:", cnt)
            # print_board(visited)

    village.sort()
    print(len(village), *village, sep="\n")


if __name__ == "__main__":
    main()
