def count_changes(board, x, y):
    white_start = 0
    black_start = 0
    for i in range(8):
        for j in range(8):
            current = board[x+i][y+j]
            if (i + j) % 2 == 0:
                if current != 'W':
                    white_start += 1
                if current != 'B':
                    black_start += 1
            else:
                if current != 'B':
                    white_start += 1
                if current != 'W':
                    black_start += 1
    return min(white_start, black_start)

def main():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    min_change = float('inf')
    for i in range(N - 7):
        for j in range(M - 7):
            changes = count_changes(board, i, j)
            min_change = min(min_change, changes)

    print(min_change)

if __name__ == "__main__":
    main()