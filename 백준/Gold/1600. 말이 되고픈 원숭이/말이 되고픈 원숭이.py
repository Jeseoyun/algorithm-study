from collections import deque


def bfs(board, W, H, K):
    queue = deque([(0, 0, 0, 0)])
    visited = [[[False]*(K+1) for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = True

    dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    h_dxy = [(-2, -1), (-1, -2), (1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1)]

    while queue:
        x, y, dist, used = queue.popleft()

        if (x, y) == (H-1, W-1):
            return dist

        if used < K:  # 말처럼 이동
            for dx, dy in h_dxy:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if visited[nx][ny][used+1]:
                    continue
                if board[nx][ny] == 1:
                    continue

                visited[nx][ny][used+1] = True
                queue.append((nx, ny, dist+1, used+1))

        for dx, dy in dxy:  # 일반 이동
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if visited[nx][ny][used]:
                continue
            if board[nx][ny] == 1:
                continue

            visited[nx][ny][used] = True
            queue.append((nx, ny, dist + 1, used))

    return -1


def main():
    K = int(input())
    W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    dist = bfs(board, W, H, K)
    print(dist)


if __name__ == "__main__":
    main()