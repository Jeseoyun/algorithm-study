import heapq

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌

def dijkstra(distance, arr, N, M):
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        cost, r, c = heapq.heappop(q)

        if cost > distance[r][c]:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:  # 범위를 벗어나거나 이미 방문했으면 진행x
                continue

            if cost + arr[nr][nc] < distance[nr][nc]:
                distance[nr][nc] = cost + arr[nr][nc]
                heapq.heappush(q, (distance[nr][nc], nr, nc))


def main():
    M, N = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    
    INF = float('inf')
    distance = [[INF] * M for _ in range(N)]
    
    dijkstra(distance, arr, N, M)
    print(distance[N - 1][M - 1])
    

if __name__ == "__main__":
    main()