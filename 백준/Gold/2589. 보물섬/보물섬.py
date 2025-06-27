from collections import deque


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def main():
    N, M = map(int, input().split())
    land = [[_ for _ in input()] for _ in range(N)]

    # 1. 시작 지점 찾기
    start_pos = []
    for i in range(N):
        for j in range(M):
            if land[i][j] == "L":
                start_pos.append((i, j))

    # 2. bfs 탐색: 최소 도달 가능 경로
    # 시작 지점으로부터 모든 지점까지의 도달 가능한 거리 중 최댓값 = 보물이 묻힌 곳의 거리
    max_cost = 0
    for sx, sy in start_pos:
        queue = deque([(sx, sy, 0)])
        visited = [[0]*M for _ in range(N)]
        visited[sx][sy] = 1

        while queue:
            x, y, cost = queue.popleft()

            for dx, dy in dxy:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                if visited[nx][ny]:
                    continue

                if land[nx][ny] == "W":
                    continue

                visited[nx][ny] = 1
                queue.append((nx, ny, cost+1))
                max_cost = max(max_cost, cost+1)

    print(max_cost)


if __name__ == "__main__":
    main()