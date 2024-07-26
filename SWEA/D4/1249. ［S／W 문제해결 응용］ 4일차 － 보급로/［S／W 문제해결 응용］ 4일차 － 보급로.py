from collections import deque
 
 
def restore_road(road, x, y):
    dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    queue = deque([[x, y]])  # 출발지점
 
    accumulated_time = [[float('inf')]*N for _ in range(N)]
 
    accumulated_time[x][y] = road[x][y]  # 출발 지점에서 수리 시간
 
    while queue:
        x, y = queue.popleft()
 
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
 
            # 이동 범위를 벗어난 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
 
            new_time = accumulated_time[x][y] + road[nx][ny]
            if new_time < accumulated_time[nx][ny]:
                accumulated_time[nx][ny] = new_time
                queue.append([nx, ny])
    return accumulated_time[N-1][N-1]
 
 
T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
 
    result = restore_road(road, 0, 0)
 
    print(f"#{test_case} {result}")