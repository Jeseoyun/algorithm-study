from collections import deque


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def comb(arr, idx, n, curr, result):
    # arr 내에서 n개 선택하는 경우의 수
    if len(curr) == n:
        result.append(curr)
        return

    if idx >= len(arr):
        return

    comb(arr, idx+1, n, curr+[arr[idx]], result)
    comb(arr, idx+1, n, curr, result)


def bfs(grid, N, M, g_start, r_start):
    queue = deque([])
    visited = [[[-1]*2 for _ in range(M)] for __ in range(N)]
    flower = [[False]*M for _ in range(N)]
    flowers = 0

    # green
    for sx, sy in g_start:
        queue.append((sx, sy, 0, 0))  # x, y, t, color
        visited[sx][sy][0] = 0

    # red
    for sx, sy in r_start:
        queue.append((sx, sy, 0, 1))
        visited[sx][sy][1] = 0

    while queue:
        # print(queue)
        x, y, t, color = queue.popleft()

        if flower[x][y]:
            continue

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if grid[nx][ny] == '0':
                continue

            if flower[nx][ny]:
                continue

            if visited[nx][ny][color^1] == t+1:
                flower[nx][ny] = True
                flowers += 1
                continue

            if visited[nx][ny][color] == -1 and visited[nx][ny][color^1] == -1:
                queue.append((nx, ny, t+1, color))
                visited[nx][ny][color] = t + 1

    return flowers


def main():
    N, M, G, R = map(int, input().split())
    garden = [input().split() for _ in range(N)]
    # print(garden)

    # 1. 배양액 뿌릴 수 있는 칸 찾기
    # 0: 호수, 1: 불가, 2: 가능
    init_pos = []
    for i in range(N):
        for j in range(M):
            if garden[i][j] == '2':
                init_pos.append((i, j))
    # print("init_pos:", init_pos)

    # 2. 초록색 / 빨간색 배양액 뿌릴 조합 찾기
    candidates = []
    comb(init_pos, 0, G+R, [], candidates)
    # print("candidates:", candidates)

    # 3. 조합마다 배양액 확산 시켜서 꽃 핀 곳 찾기
    max_flower = 0
    for picked in candidates:
        # print("picked:", picked)
        greens = []
        comb(picked, 0, G, [], greens)

        for green in greens:
            # print("green:",green)
            red = [pos for pos in picked if pos not in green]
            # print("red:",red)

            # 4. 최대 경우 찾기
            max_flower = max(max_flower, bfs(garden, N, M, green, red))

    print(max_flower)


if __name__ == "__main__":
    main()