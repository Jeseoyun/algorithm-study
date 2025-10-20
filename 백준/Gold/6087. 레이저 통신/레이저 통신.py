from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
opposite = {0: 1, 1: 0, 2: 3, 3: 2}

INF = float('inf')


def direction_changed(start, end, jidoh, W, H):
    visited = [[[INF]*4 for _ in range(W)] for _ in range(H)]
    queue = deque()

    sx, sy = start
    ex, ey = end

    for d in range(len(dxy)):
        visited[sx][sy][d] = 0

    queue.append((sx, sy, -1, 0))

    while queue:
        x, y, d, changed = queue.popleft()

        for nd, (dx, dy) in enumerate(dxy):
            nx, ny = x + dx, y + dy
            new_changed = changed + (0 if d == -1 or d == nd else 1)

            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue

            if jidoh[nx][ny] == '*':
                continue

            if d != -1 and nd == opposite[d]:
                continue

            if visited[nx][ny][nd] <= new_changed:
                continue

            if d == -1 or d == nd:
                queue.appendleft((nx, ny, nd, new_changed))
            else:
                queue.append((nx, ny, nd, new_changed))

            visited[nx][ny][nd] = new_changed

    return min(visited[ex][ey])


def main():
    W, H = map(int, input().split())
    jidoh = [list(input()) for _ in range(H)]

    # 1. 시작지점, 도착지점 찾기
    points = [(x, y) for x in range(H) for y in range(W) if jidoh[x][y] == 'C']
    start, end = points

    # 2. 시작지점 -> 도착지점 방향 전환 몇 번 했는지
    min_mirror = direction_changed(start, end, jidoh, W, H)
    print(min_mirror)


if __name__ == "__main__":
    main()