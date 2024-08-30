from collections import deque


dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
click_count = 0


def calculate_mine(grid, N, visited):
    for x in range(N):
        for y in range(N):
            # 지뢰는 방문하지 않기 위해 그냥 방문 체크 해버림
            if grid[x][y] == "*":
                visited[x][y] = 1
                continue

            neighbor_mine = 0
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if grid[nx][ny] == "*":
                    neighbor_mine += 1

            grid[x][y] = neighbor_mine


def click(grid, grid_size, sx, sy, visited):
    queue = deque([])
    queue.append((sx, sy))

    visited[sx][sy] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= grid_size or ny < 0 or ny >= grid_size:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1

            if grid[nx][ny] == 0:
                queue.append((nx, ny))


def main():
    global click_count

    T = int(input())

    for test_case in range(1, T+1):
        N = int(input())
        grid = [list(input()) for _ in range(N)]
        visited = [[0]*N for _ in range(N)]

        # 주변의 지뢰 개수를 계산해서 값을 집어넣는다
        calculate_mine(grid, N, visited)

        click_count = 0

        # 최소 클릭으로 지뢰를 제외한 모든 칸을 열기
        for i in range(N):
            for j in range(N):
                # 1) 0으로 찍혀있는 부분 먼저 클릭 (많은 칸을 먼저 열어놓기 위해)
                if grid[i][j] == 0 and visited[i][j] == 0:
                    click_count += 1
                    click(grid, N, i, j, visited)
        
        # 2) 나머지 열리지 않은 부분까지 모두 열면 지뢰 빼고 모두 방문 완료
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    click_count += 1
        print(f"#{test_case} {click_count}")


if __name__ == "__main__":
    main()