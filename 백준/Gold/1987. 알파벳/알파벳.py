dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
max_len = 0


def dfs(board, R, C, x, y, visited, history):
    global max_len
    # print("x, y:", (x, y), board[x][y])
    max_len = max(max_len, len(history))

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        if visited[nx][ny]:
            continue

        if board[nx][ny] in history:
            continue

        visited[nx][ny] = True
        history.add(board[nx][ny])

        dfs(board, R, C, nx, ny, visited, history)

        visited[nx][ny] = False
        history.remove(board[nx][ny])


def main():
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]

    visited = [[False]*C for _ in range(R)]
    visited[0][0] = True
    history = set(board[0][0])
    dfs(board, R, C, 0, 0, visited, history)

    print(max_len)


if __name__ == "__main__":
    main()