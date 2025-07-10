
BOGGLE_BOARD_SIZE = 4
MAX_WORD_LEN = 8
dxy = [(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def dfs(board, x, y, visited, path, found, vocab):
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= BOGGLE_BOARD_SIZE or ny < 0 or ny >= BOGGLE_BOARD_SIZE:
            continue

        if visited[nx][ny]:
            continue

        if len(path) > MAX_WORD_LEN:  # 글자 수 초과하면 더 이상 탐색 안해도 됨
            continue

        if path + board[nx][ny] in vocab:
            found.add(path + board[nx][ny])

        visited[nx][ny] = 1
        dfs(board, nx, ny, visited, path + board[nx][ny], found, vocab)
        visited[nx][ny] = 0


def main():
    w = int(input())
    vocab = {input() for _ in range(w)}
    _ = input()  # 공백

    b = int(input())

    for idx in range(b):
        if idx != 0:
            _ = input()  # 공백

        board = [list(input()) for _ in range(BOGGLE_BOARD_SIZE)]

        found = set()
        for sx in range(BOGGLE_BOARD_SIZE):
            for sy in range(BOGGLE_BOARD_SIZE):
                # print((sx, sy), f"시작: {board[sx][sy]}")
                # found = bfs(board, sx, sy, vocab)
                visited = [[0] * BOGGLE_BOARD_SIZE for _ in range(BOGGLE_BOARD_SIZE)]
                visited[sx][sy] = 1
                dfs(board, sx, sy, visited, board[sx][sy], found, vocab)
        # print(found)

        score = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}
        max_len_word = ""
        total_score = 0

        for word in sorted(list(found)):
            total_score += score[len(word)]

            if len(word) > len(max_len_word):
                max_len_word = word

        print(total_score, max_len_word, len(found))



if __name__ == "__main__":
    main()