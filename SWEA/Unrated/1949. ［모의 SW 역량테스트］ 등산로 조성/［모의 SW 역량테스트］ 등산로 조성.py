dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_length = 0


def find_highest_point(map, map_size):
    max_height = 0
    hp = []
    for i in range(map_size):
        for j in range(map_size):
            if max_height < map[i][j]:
                max_height = map[i][j]
                hp = []
            if max_height == map[i][j]:
                hp.append((i, j))
    return hp


def dfs(hiking_map, map_size, x, y, visited, path, K, FLAG=False):
    global max_length

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        
        # 배열 범위 벗어나는 경우
        if nx < 0 or nx >= map_size or ny < 0 or ny >= map_size:
            continue

        # 이미 방문한 곳일 경우
        if visited[nx][ny]:
            continue

        # 다음 지점의 높이가 현재 지점의 높이보다 낮으면 방문 가능
        if hiking_map[nx][ny] < path[-1]:
            visited[nx][ny] = 1
            path.append(hiking_map[nx][ny])

            max_length = max(max_length, len(path))

            dfs(hiking_map, map_size, nx, ny, visited, path, K, FLAG)

            visited[nx][ny] = 0
            path.pop(-1)

        # 단 1회, 지형을 깎을 수 있다
        elif not FLAG and hiking_map[nx][ny] - K < path[-1]: 
            FLAG = True

            visited[nx][ny] = 1
            path.append(path[-1] - 1)  # 이전 지점보다 딱 1 낮게 깎으면 최소로 깎는 거시다

            max_length = max(max_length, len(path))

            dfs(hiking_map, map_size, nx, ny, visited, path, K, FLAG)

            FLAG = False
            visited[nx][ny] = 0
            path.pop(-1)



def main():
    global max_length

    T = int(input())

    for test_case in range(1, T+1):
        N, K = map(int, input().split())
        hiking_map = [list(map(int, input().split())) for _ in range(N)]
        highest_points = find_highest_point(hiking_map, N)

        max_length = 0
        for start_point in highest_points:
            sx, sy = start_point
            visited = [[0] * N for _ in range(N)]
            path = []

            visited[sx][sy] = 1
            path.append(hiking_map[sx][sy])

            dfs(hiking_map, N, sx, sy, visited, path, K)
            
        print(f"#{test_case} {max_length}")


if __name__ == "__main__":
    main()