from collections import deque


def solution(maps):
    dxy = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    costs = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    queue = deque([(0, 0)])
    costs[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        # print(queue, costs[x][y])
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            
            # 맵 밖을 벗어난 경우
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            
            # 갈 수 없는길일 경우
            if maps[nx][ny] == 0:
                continue
            
            # 이미 한 번 방문한 경우
            if costs[nx][ny] > 0:
                continue
            
            costs[nx][ny] = costs[x][y] + 1  # 누적 거리 저장
            queue.append((nx, ny))
            
            if nx == len(maps)-1 and ny == len(maps[0])-1:
                return costs[nx][ny]

    return -1  # 상대 팀 진영에 도달하지 못한 경우