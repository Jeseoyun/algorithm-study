dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
max_len = 0


def dfs(board, R, C, x, y, alphabet, history):
    global max_len
    # print("x, y:", (x, y), board[x][y])
    max_len = max(max_len, len(history))

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        alp_idx = ord(board[nx][ny])- ord('A')

        if alphabet[alp_idx]:
            continue

        if board[nx][ny] in history:
            continue


        alphabet[alp_idx] = True
        history.add(board[nx][ny])

        dfs(board, R, C, nx, ny, alphabet, history)

        alphabet[alp_idx] = False
        history.remove(board[nx][ny])


def main():
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]

    alphabet = [False]*26  # 26개
    history = set(board[0][0])
    dfs(board, R, C, 0, 0, alphabet, history)

    print(max_len)


if __name__ == "__main__":
    main()