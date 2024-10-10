from collections import deque


def bfs(sx, sy):
    danji_cnt = 1
    queue = deque([(sx, sy)])
    dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue

            if danji[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                danji_cnt += 1

    return danji_cnt


N = int(input())
danji = [list(map(int, input())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]

danji_num = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and danji[i][j]==1:
            visited[i][j] = 1
            danji_num.append(bfs(i, j))

sorted_danji_num = sorted(danji_num)
print(len(danji_num), end="")
for dn in sorted_danji_num:
    print()
    print(dn, end="")