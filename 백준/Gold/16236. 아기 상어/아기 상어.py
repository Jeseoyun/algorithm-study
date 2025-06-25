from collections import deque


dxy = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 왼쪽이 우선순위 1번, 위쪽이 우선순위 2번


def bfs(space, N, sx, sy, shark_size):
    fishes = []
    min_dist = float('inf')

    queue = deque([(sx, sy, 0)])
    visited = [[0]*N for _ in range(N)]
    visited[sx][sy] = 1

    while queue:
        x, y, t = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            if space[nx][ny] > shark_size:
                continue

            visited[nx][ny] = 1
            queue.append((nx, ny, t + 1))

            if 0 < space[nx][ny] < shark_size:
                if t + 1 <= min_dist:
                    min_dist = t + 1
                    fishes.append((t + 1, nx, ny))

    fishes = [f for f in fishes if f[0] == min_dist]
    fishes.sort()
    return fishes  # (distance, x, y)




def main():
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]

    # 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                sx, sy = i, j
                space[i][j] = 0

    shark_size = 2
    eat_count = 0
    time = 0

    while True:
        fishes = bfs(space, N, sx, sy, shark_size)
        if not fishes:
            break

        dist, x, y = fishes[0]
        time += dist
        eat_count += 1
        space[x][y] = 0
        sx, sy = x, y

        if eat_count == shark_size:
            shark_size += 1
            eat_count = 0

    print(time)


if __name__ == "__main__":
    main()